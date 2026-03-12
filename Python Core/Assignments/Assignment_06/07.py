"""
        A
      A B C
    A B C D E
  A B C D E F G

"""

n = int(input("Enter the number: "))

for i in range(1, n+1):
    for j in range(1,n+1-i):
        print(" ",end = " ")
    for j in range(1,2*i):
        print(chr(64 + j),end = " ")
    print()