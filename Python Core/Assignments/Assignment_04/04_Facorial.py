# 4. WAP to print factorial of a number .

# Using For
'''
x = int(input("Enter the number : "))

fact = 1

for i in range(1,x+1):
    fact *= i
print(f"Factorial of {x} is : {fact}")
'''


# Using While

y = int(input("Enter the number : "))

fact = 1
i = 1

while (i <= y):
    fact *= i
    i += 1
print(f"Factorial of {y} is : {fact}")