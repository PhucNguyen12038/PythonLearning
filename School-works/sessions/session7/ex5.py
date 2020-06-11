s1 = input("Enter word: ")
s2 = input("Enter rhyme-word: ")
maxi = 0
maxWord = ""
while s2 != 'done':
    
    length1 = len(s1) - 1
    length2 = len(s2) - 1
    min_length = length1
    if min_length > length2:
        min_length = length2
    stop = False
    count = 0
    while min_length > 0:
        if s1[length1] == s2[length2]:
            count += 1
            min_length -= 1
            length1 -= 1
            length2 -= 1
        else:
            break
    print("Rhyme score is {}".format(count))
    if count > maxi:
        maxi = count
        maxWord = s2    
    s2 = input("Enter rhyme-word: ")   
print("The word with the highest rhyme score was '{}', its score was {}.".format(maxWord,maxi))            
