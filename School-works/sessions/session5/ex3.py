#! /usr/bin/python3


import random


def main():
    num = int(input("Enter the numbers of shoe for door:"))
    door1 = num
    door2 = num
    count = 0
    while True:
        count += 1
        r1 = random.random()
        if r1 > 0.5:
            door1 -= 1
        else:
            door2 -= 1

        if door1 < 0 or door2 < 0:
            print("No shoe any more!")
            return count
            

        r2 = random.random()
        if r2 > 0.5:
            door1 += 1
        else:
            door2 += 1
        print("Turn: {}".format(count))
        print("The number of shoes are {}, {}\n".format(door1, door2))
        
s = 0
for i in range (0, 20):
    r = main()
    s = s + r
s = s / 20
print(s)