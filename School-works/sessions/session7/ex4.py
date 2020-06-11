open_char = ['{','[','(']
close_char = ['}',']',')']
filter_char = ['{','[','(','}',']',')']

s = input("Enter string: ")
filter_s = ""
stack = []

for i in s:
    for j in filter_char:
        if i == j:
            filter_s = filter_s + i

length = len(filter_s)
if length % 2 == 0:
    
    stop = False
    for i in filter_s:
        for j in open_char:
            if i == j:
                stack.append(i)
        #print("push open: ",stack)
        for k in close_char:
            if i == k:
                top = stack.pop()
                current = i
                for l in range (0,len(open_char)):
                    if top == open_char[l]:
                        index1 = l
                        break
                for p in range (0, len(close_char)):
                    if current == close_char[p]:
                        index2 = p
                        break
                if index1 != index2:
                    print("not balanced")
                    exit()
                #print("stack is ",stack)
    print("balanced")
else:
    print("not balanced")
