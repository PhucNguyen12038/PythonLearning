def test_palindrome(n):
    str_n = str(n)
    length = int(len(str_n))
    count = 0
    for i in range(0,int(length / 2)):
        if str_n[i] == str_n[length-1-i]:
            count +=1
    if count == int(length / 2):
        return True
    else:
        return False
    
def reverse_str(x):
  return x[::-1]

i = input("Enter number: ")
count = 0
t = i
while test_palindrome(t) == False:
    reverse_t = reverse_str(str(t))
    a = int(reverse_t)
    i = int(t)
    t = i + a
    count += 1
    print(t)
print(count)