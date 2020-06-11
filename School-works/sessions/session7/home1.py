n = input("Enter first name: ")
g = input("Enter grades: ")

n = n.lower()
n = n.replace(n[0], n[0].upper())

g = g.upper()
print("Hello {}, your grades are {}".format(n,g))

num_of_grade = len(g)
print("You have {} grades".format(num_of_grade))
last_grade = g[num_of_grade-1]
print("Last grade is {}".format(last_grade))
count = 0
for i in g:
    if i == "A" or i == "B":
        count +=1
        
print("The number of A's and B's is {}".format(count))