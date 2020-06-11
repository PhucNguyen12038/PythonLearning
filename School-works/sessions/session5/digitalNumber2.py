
def display (n,size):
    width = size + 2
    height = (size + 1)*2+1
    count = 0
    while n != 0:
        a = n % 10
        n = n // 10
        distance = (count+1) * 3
        count += 1
        if a == 0:
            for i in range (0,height):
                for j in range (0, distance):
                    print(" ", end='')
                for j in range (0,width):
                    if i == 0 or i == height-1:
                        if j == 0 or j == width-1:
                            print(" ", end='')
                        else:
                            print("-", end='')
                    elif i == int(height/2):
                        print(" ",end='')
                        
                    else:
                         if j == 0 or j == width-1:
                             print("|", end='')
                         else:
                             print(" ",end='')
                             
                print("\n")

        if a == 1:
            for i in range (0,height):
                for j in range (0, distance):
                    print(" ", end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        print(" ", end='')
                    else:
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                print("\n") 

         
        if a == 2:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    elif i >= 1 and i < int(height/2):
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    else:
                        if j == 0:
                            print("|", end='')
                        else:
                            print(" ", end='')
                print("\n") 

        if a == 3:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    else:
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    
                print("\n") 
        

        if a == 4:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == int(height/2):
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    elif i >= 1 and i < int(height/2):
                        if j == 0 or j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    elif i == 0 or i == height-1:
                        print(" ", end='')
                    else:
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                print("\n")

        if a == 5:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    elif i >= 1 and i < int(height/2):
                        if j == 0:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    else:
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                print("\n")
                
        if a == 6:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    elif i >= 1 and i < int(height/2):
                        if j == 0:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    else:
                        if j == 0 or j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                print("\n")

        if a == 7:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == 0:
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    elif i == int(height/2) or i == height-1:
                        print(" ", end='')
                    else:
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    
                print("\n")

        if a == 8:
            for i in range (0,height):
                for j in range (0, distance):
                    print(" ", end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        if j == 0 or j == width-1:
                            print(" ", end='')
                        else:
                            print("-", end='')
                    elif i == int(height/2):
                        print(" ",end='')
                        
                    else:
                         if j == 0 or j == width-1:
                             print("|", end='')
                         else:
                             print(" ",end='')
                             
                print("\n")

        if a == 9:
            for i in range (0,height):
                for j in range (0,distance):
                    print(" ",end='')
                for j in range (0,width):
                    if i == 0 or i == height-1 or i == int(height/2):
                        if j >= 1 and j < int(height/2):
                            print("-", end='')
                        else:
                            print(" ", end='')
                    elif i >= 1 and i < int(height/2):
                        if j == width-1 or j == 0:
                            print("|", end='')
                        else:
                            print(" ", end='')
                    else:
                        if j == width-1:
                            print("|", end='')
                        else:
                            print(" ", end='')
                print("\n")

array = []
number = input("Enter number: ")
try:
    n = int(number)
except:
    n = -1

if n == -1:
    print("Invalid number")
else:
    size = input("Enter size: ")
    try:
        s = int(size)
    except:
        s = -1

    if s == -1:
        print("Invalid size")
    else:
        display(n,s)
        


           
