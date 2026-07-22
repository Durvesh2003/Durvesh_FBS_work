"""
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))

try:
    res = a // b
    print(res)
except :
    print( " You cannot divide by zero")

"""

"""
# Specialized exception used
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
try:
    res = a // b
    print(f"Result : {res}")
    num = int(input("enter vthe numberrrr : "))
    for i in num:
        print(i)
except ZeroDivisionError as s :
    print(f"code run with exception {s}")

except ValueError as v:
    print(f"I am valueError {v}")

except Exception as e:
    print(f"Generalised Exception {e}")

else:
    print("I am in else block")
"""

a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
def func():
    try :
        res = a//b
        return res
    # except ZeroDivisionError as s:
    #     print("not divisible by zero")
    finally:
        print(" I am inside function finally")

print(func())

n = int(input("Enter the number :"))
if n < 0:
    raise Exception("I am not good")
print(f"Number is {n}")
