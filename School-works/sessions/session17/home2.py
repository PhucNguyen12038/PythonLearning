
def levels_depth(obj,depth):
    if type(obj) != list:
        return 0

    i = 1    
    
    for item in obj:
        if type(item) == type([]):
            levels_depth(item,depth+1)        
    
        else:
            obj[i-1] = depth
            
        
        i +=1
    return obj

def levels(obj):   
    return levels_depth(obj,1)
    

a = [17, [69, [25], [[74], 43], 66], 98]
b = [8, [6, 7, [-1], [4, [[10]]], 2], 1]
c = [8,5,[2]]
print(levels(c))
