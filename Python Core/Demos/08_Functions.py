def addition():
    a = int(input("enter the number1 : "))
    b = int(input("enter the number1 : "))

    sum = a + b
    print(f"sum of {a} and {b} is {sum}")

addition()


# types based on input and output

# 1. without passing parameters and without returning value
def addition():
    a = int(input("enter the number1 : "))
    b = int(input("enter the number1 : "))

    sum = a + b
    print(f"sum of {a} and {b} is {sum}")

addition()

# 2. with passing parameters and without returning value
def addition(a,b):
    sum = a + b
    print(f"sum of {a} and {b} is {sum}")
a = int(input("enter the number1 : "))
b = int(input("enter the number1 : "))
addition(a,b)

# 3. without passing parameters and with returning value
def addition():
    a = int(input("enter the number1 : "))
    b = int(input("enter the number1 : "))
    sum = a + b
    return sum

res = addition()
print(f'addition is {res}')

# 4. with passing parameters and with returning value
def addition(a,b):

    sum = a + b
    return sum
a = int(input("enter the number1 : "))
b = int(input("enter the number1 : "))
res = addition(a,b)
print(f'addition of numbers is {res}')


# default parameter with positional argument concept

def add(num1,num2,num3=2,num4=5):
    sum = num1 + num2 + num3 + num4
    print(sum)
add(10,20)

# keyword parameter concept
#1. to neglect position parameter concept
#2. Assigning value to parameter in function call
#3. Name of parameter in function call and func defination should be same

def emp(id,name,salary,dept):
    print("Id: ",id)
    print("name: ",name)
    print("Salary: ",salary)
    print("Department: ",dept)

emp(101,'ABC',200000,"DA")
print("##############################")
emp(name = "XYZ", salary= 800000,dept="Testing",id=102)

# Variable Length Parameter/Argument

def add(a,*numbers):
    sum=0
    for num in numbers:
        sum += num
    return sum
res = add('a',10,20,30,40)
print(res)

# Keyword variabvle length paramter/argument

def emp(**data):
    print(data)
emp(id=101,name='ABC',sal=35000)

def emp(**data):
    for key,value in data.items():
        print(f'{key} : {value}')
emp(id=101,name='ABC',sal=35000)

def dummy(*args,**kwargs):
    print(args)
    print(kwargs)

dummy(10,20,30,40,id = 101,name = "ABC" , salary = 100000)
