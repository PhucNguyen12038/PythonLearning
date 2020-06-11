
def levels_helper(lst, depth):                 # Helper function
    
    levels = []
    for el in lst:
        if isinstance(el,list):
            levels.append(levels_helper(el, depth + 1)) 
        else:
            levels.append(depth)
    
    return levels
def levels(lst):                               # Main function
    lst = levels_helper(lst, 1)
    return lst
    

a = [17, [69, [25], [[74], 43], 66], 98]
b = [8, [6, 7, [-1], [4, [[10]]], 2], 1]
c = [8,5,[2]]
print(levels(c))