flights = {'Paris': {'London', 'Berlin', 'Nice'}, 'London': {'Berlin',
'Paris'}, 'Berlin': {'London', 'Paris', 'Tallinn'}, 'Tallinn': {'Berlin'}}

def find_line(familytree, descendant, ancestor):
    
    # Base case. If descendant is the same as ancestor,
    # then the line consists of one individual only
    # and we return an one-element list.
    if descendant == ancestor:
        return [descendant]
    
    # If the descendant exists in the dictionary, then it is possible that
    # there exists a line of decent through his/her parents.
    if descendant in familytree:
        
        # Check all parents of the descendant in the dictionary
        for parent in familytree[descendant]:
            
            # Try to find the line from the parent to the ancestor
            line = find_line(familytree, parent, ancestor)
            
            # If found, then add the descendant at the beginning of the line
            # and return the line
            if line != []:
                return [descendant] + line
            
    # If we reach this point, then all seaches were unsuccessful
    # and we return empty list
    return []
print(find_line(flights,'Tallinn','Paris'))