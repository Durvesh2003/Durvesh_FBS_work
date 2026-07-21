x = 5
y = 10


# Method 1
# import My_module
# print(My_module.Addition(x,y))
# print(My_module.Multiplication(x,y))


# method 2
# from My_module import *
# print(Addition(x,y))

# method 3
# from My_module import Addition,Subtraction
# print(Addition(x,y))
# print(Subtraction(x,y))

# method 4
from My_module import Addition as add
print(add(x,y))

