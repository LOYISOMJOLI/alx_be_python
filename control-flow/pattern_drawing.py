size = int(input("Enter the size of the pattern:"))
row  = 1
while row <= size:
    col = 1
    while col <= size:
        print("*", end="")
        col += 1
    print()
row -= 1
