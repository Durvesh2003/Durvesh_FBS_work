# Pass  

for i in range(1,10):
    pass

# Break

# for i in range (1,6):
#     if(i == 3):
#         break
#     print(i)

# Continue 

for i in range (1,6):
    if(i == 3):
        continue
    print(i)

# else : else part is executed  when loop executed successfully 
# eg

for i in range(1,6):
    if(i == 3):
        continue
    print(i)
else :
    print("Else Block executed")


num = int(input("Enter the number : "))
for i in range(2,num):
    if(num%i == 0):
        print(f"{num} is not a prime number")
else :
    print(f"{num} is a Prime number")