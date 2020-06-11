def number_of_bags(n):
    if n == 1:
        return 2
    else:
        if (n-1) % 3 == 0:
            return number_of_bags(n-1)+2
        else:
            return number_of_bags(n-1)+1

print(number_of_bags(8))