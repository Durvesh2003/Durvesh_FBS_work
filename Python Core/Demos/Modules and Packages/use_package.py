# method1
from my_package import module
print(module.Addition(10,10))

# mehod 2
from my_package.module import *
print(Addition(10,20))

# method 3
from my_package.module import Multiplication
print(Multiplication(10,20)) 

# method 4
from my_package.module import Subtraction as sub
print(sub(20,10))