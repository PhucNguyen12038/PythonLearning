import random

number = random.randint(1,10)
print(number)
stop = False
while stop == False:
    guess = int(input("Guess number: "))
    if guess < number:
        print("larger")
    elif guess > number:
        print("smaller")
    else:
        print("correct")
        stop = True

