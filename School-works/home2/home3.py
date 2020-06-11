l = input("Enter the length of power line: ")
d = input("Enter the max distance: ")

lengthOfLine = int(l)
maxDist = int(d)
result = 0
if (lengthOfLine <= maxDist):
    result = result + 2
else:
    divisor = lengthOfLine // maxDist
    result = result + 2 + divisor
    if(divisor == lengthOfLine / maxDist):
        result = result - 1
print(result)