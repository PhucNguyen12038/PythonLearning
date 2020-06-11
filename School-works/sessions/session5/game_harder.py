import random
head = 1
tail = 1000
number = int(input("Enter the number: "))
stop = False
while stop == False:
    guess = random.randint(head,tail)
    print(guess)
    if guess < number:
        print("larger")
        head = guess + 1
    elif guess > number:
        print("smaller")
        tail = guess - 1
    else:
        print("correct")
        stop = True
    