"""
To remove "tiles", click left mouse button
To mark a probable mine, click right mouse button.

Compared to usual Minesweeper game the program is more primitive:
- Areas whose neighborhood doesn't contain mines don't open by itself,
  i.e. all squares must be clicked through.
- There is no message when the game is finished successfully. The user
  should keep count of marked mines and congratulate himself/herself
  at the right moment.
"""

from tkinter import *
from tkinter import font, messagebox
import random

# Helper function create_layout creates a random playboard
# (and computes the number of mines around each square)
# This function is independent of the rest of the program,
# since it takes all necessary information as arguments
# and returns a simple 2-dimensional array

def create_layout(row_count, col_count, mine_count):

    # First choose random positions for mines.
    # For that we create a list with all possible positions:
    all_positions = []
    for x in range(col_count):
        for y in range(row_count):
            all_positions.append((x, y))

    # and choose randomly a correct number of elements from there
    mine_positions = random.sample(all_positions, mine_count)

    # Place mines and numbers in the matrix that represents the board
    layout = []
    for y in range(row_count): # for all rown numbers
        row = []
        for x in range(col_count): # .. and all column numbers
            if (x,y) in mine_positions:
                row.append("☼")
            else:
                # This square has no mine. Need to count how many bombs are in its neighborhood
                # The fact that squares at the edge of the board have less neighbours
                # than the squares at the center, makes things more complex.
                neighbor_mine_count = 0
                
                # left
                if x > 0 and (x-1, y) in mine_positions:
                    neighbor_mine_count += 1
                
                # top
                if y > 0 and (x, y-1) in mine_positions:
                    neighbor_mine_count += 1
                    
                # right
                if x < col_count+1 and (x+1, y) in mine_positions:
                    neighbor_mine_count += 1
                
                # bottom
                if y < row_count+1 and (x, y+1) in mine_positions:
                    neighbor_mine_count += 1
                
                # top-left
                if y > 0 and x > 0 and (x-1, y-1) in mine_positions:
                    neighbor_mine_count += 1
                
                # top-right
                if x < col_count+1 and y > 0 and (x+1, y-1) in mine_positions:
                    neighbor_mine_count += 1
                
                # bottom-right
                if y < row_count+1 and x < col_count+1 and (x+1,y+1) in mine_positions:
                    neighbor_mine_count += 1
                    
                # bottom-left
                if x > 0 and y < row_count+1 and (x-1, y+1) in mine_positions:
                    neighbor_mine_count += 1
                        
                row.append(neighbor_mine_count)
        layout.append(row)
    
    return layout
    
# Main program ###################################################################
# Prepare playboard
row_count = 10
col_count = 7
tile_size = 32 # length of one square in pixels
mine_count = 10

# Tk creates program main windows
root = Tk()
root.title("Minesweeper")

# Canvas is a widget where we can put drawings, images etc on.
canvas = Canvas(root, width=col_count*tile_size, height=row_count*tile_size, highlightthickness=0)
canvas.pack()

statusbar = Label(root, text="The board has %d mines" % mine_count, bd=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

big_font = font.Font(family='Helvetica', size=12, weight='bold')
#canvas.create_text(30, 50, text="Hello!", font=big_font, anchor=NW)


# Create the "bottom layer" of the board on Canvas
layout = create_layout(row_count, col_count, mine_count)
# Place mines and numbers graphically on the board
for y in range(row_count): # go through all row numbers
    for x in range(col_count): # .. and all column numbers
        tile_text = str(layout[y][x])
        canvas.create_rectangle(x*tile_size, 
                                y*tile_size,
                                x*tile_size+tile_size, 
                                y*tile_size+tile_size)
        
        # write a mine symbol or number of mines in the neighborhood inside the square
        canvas.create_text(x*tile_size + 10, 
                           y*tile_size + 5, 
                           text=tile_text, 
                           font=big_font, 
                           anchor=NW)

# Now the lower layer is ready
# Next we cover the board with images
# First load the images
plain_cover_img = PhotoImage(file="plain_cover.gif", name="plain_cover")
flagged_cover_img = PhotoImage(file="flagged_cover.gif", name="flagged_cover") # this image is needed later

# Functions right_click and left_click are associated with mouse clicks below
def right_click(event):
    # Find out on which image (square) the the user clicked
    item_id = event.widget.find_closest(event.x, event.y)[0]

    # if it is image of flag, then change to the image without flag
    # and other way around
    if canvas.itemcget(item_id, 'image') == "plain_cover":
        canvas.itemconfig(item_id, image=flagged_cover_img)
    else:
        canvas.itemconfig(item_id, image=plain_cover_img)
    # TODO: congratulations when all bombs are marked

def left_click(event):
    item_id = event.widget.find_closest(event.x, event.y)[0]
    # remove tile
    canvas.delete(item_id)

    # find out in what row / column it is
    x = event.x // tile_size
    y = event.y // tile_size
    if layout[y][x] == "☼":
        messagebox.showinfo("Game over!", "You stepped on a mine, game over!")
        exit()


# Create images of tiles and associate them with mouse clicks
# Also store the tiles
for y in range(row_count):
    for x in range(col_count):
        img_id = canvas.create_image(x*tile_size, y*tile_size, anchor=NW, image=plain_cover_img)
        canvas.tag_raise(img_id) 
        canvas.tag_bind(img_id, "<1>", left_click)
        canvas.tag_bind(img_id, "<3>", right_click)
        
# mainloob makes board window visible and starts to wait user activities
root.mainloop()