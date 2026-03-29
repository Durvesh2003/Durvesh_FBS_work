n = int(input("Enter the number: "))

for i in range(1, n+1):

    # Left increasing numbers
    for j in range(1, i+1):
        print(j, end=" ")

    # Middle spaces
    for j in range(2*(n-i)):
        print(" ", end=" ")

    # Right decreasing numbers
    if i == n:
        for j in range(i-1, 0, -1):
            print(j, end=" ")
    else:
        for j in range(i, 0, -1):
            print(j, end=" ")

    print()