fname = "evolution.txt"

def rearrange(fname):
    try:
        ffile = open(fname)
    except:
        print("File cannot be opened:", fname)
    else:
        
        print(ffile.readline())
        

rearrange(fname)
    
        
