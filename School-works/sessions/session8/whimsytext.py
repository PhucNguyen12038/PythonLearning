fname = "evolution.txt"

def rearrange(fname):
    try:
        ffile = open(fname)
    except:
        print("File cannot be opened:", fname)
    else:
        count_line = 0
        for line in ffile:
            count_char = len(line)
            count_line += 1
        
        ffile.seek(0, 0)
        result = ""
        
        while count_char > 0:
            count_char -= 1
            for line in ffile:
                char = line[count_char]
                result = result + char
            
            ffile.seek(0, 0)
        return result

print(rearrange(fname))
    
        

