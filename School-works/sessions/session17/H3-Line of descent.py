''' Week 16, homework problem 3
Write a recursive function find_line with three parameters. The first
parameter is a family tree dictionary, and the next two parameters are
names of descendant and ancestor. The function returns a list which
describes the line of descent from the descendant to the ancestor.
'''

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

# Testing the function
    
familytree = {
  'Kalle': {'Teet', 'Maris'},
  'Maris': {'Konstantin', 'Mari'},
  'Rita': {'Teet', 'Maris'},
  'Siim': {'Teet', 'Maris'},
  'Mari': {'Karl', 'Leeni'},
  'Teet': {'Joosep', 'Adele'},
  'Adele': {'Johannes', 'Leida'},
  'Konstantin': {'Viktor', 'Jelena'},
  'Joosep': {'August', 'Emma'},
  'Viktor': {'Nikolai', 'Maria'}
}

print(find_line(familytree, 'Kalle', 'Leida'))
print(find_line(familytree, 'Adele', 'Mari'))