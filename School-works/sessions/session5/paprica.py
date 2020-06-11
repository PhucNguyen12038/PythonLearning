#! /usr/bin/python3


def main():
    # temp = 90
    # room = 20
    # time_length = 60
    temp = int(input("Enter the soup temperature:"))
    room = int(input("Enter the room temperature:"))
    time_length = int(input("Enter the time length:"))

    for t in range(time_length):
        temp = temp - ((temp - room) * 0.19)
        print(temp)


main()
