import array as arr
face = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suit = ['C','D','H','S']
cards = []
#inputFace = ['A','J','K','Q','10']
#inputSuit = ['S','H','D','C','H']

inputFace = []
inputSuit = []


for i in range (0,5):
    c = input("Enter " + str(i+1) + ". card: ")
    cards.append(c)
    for j in range (0,13):
        if c.find(face[j]) != -1:
            inputFace.append(face[j])
    
    for k in range (0,4):
        if c.find(suit[k]) != -1:
            inputSuit.append(suit[k])
            
#print(inputFace)
#print(inputSuit)

for j in range (0,5):
    if inputFace[j] == 'J':
        inputFace[j] = '11'
        
    if inputFace[j] == 'Q':
        inputFace[j] = '12'
        
    if inputFace[j] == 'K':
        inputFace[j] = '13'
        
    if inputFace[j] == 'A':
        inputFace[j] = '14'
        
intFace = []
for j in range (0,5):
    convert = int(inputFace[j])
    intFace.append(convert)
intFace.sort()

countF = 0
countS = 0
for j in range (0,4):
    if intFace[j+1] - intFace[j] == 1:
        countF = countF + 1
    if inputSuit[j+1] == inputSuit[j]:
        countS = countS + 1
if countF == 4:
    if countS == 4 and intFace[0] == 10:
        print("Royal flush")
    elif countS == 4:
        print("Straight flush")
    else:
        print("Straight")
elif countS == 4:
    print("Flush")
    
else:    
    countSameRank = 0

    for j in range (0,4):
        if intFace[j+1] == intFace[j]:
            countSameRank = countSameRank + 1
        

    if countSameRank == 3:
        threeKind = False
        onePair = False
        fourKind = False
        
        for i in range (0,2):
            if intFace[i] == intFace[i+1] and intFace[i] == intFace[i+2] and intFace[i] == intFace[i+3]:
                fourKind = True
                print("Four of a kind")
                exit(1)
        for i in range (0,3):
            if intFace[i] == intFace[i+1] and intFace[i] == intFace[i+2]:
                threeKind = True
                
        for i in range (0,4):
            if intFace[i] == intFace[i+1]:
                onePair = True
            
        if threeKind == True and onePair == True:
            print("Full house")
            
    elif countSameRank == 2:
        threeKind = False
        for i in range (0,3):
            if intFace[i] == intFace[i+1] and intFace[i] == intFace[i+2]:
                threeKind = True
        if threeKind == True:
            print("Three of a kind")
        else:
            print("Two pair")
    elif countSameRank == 1:
        print("Pair")
    else:
        print("High Card")

