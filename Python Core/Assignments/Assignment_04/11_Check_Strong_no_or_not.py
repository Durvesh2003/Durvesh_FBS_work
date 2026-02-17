# 11. WAP to check if given number Strong Number.
#  -- >  145  == 1fact + 4Fact + 5fact 
            #   == sum is 145
num = int(input("Enter the number : "))
temp = num
sum = 0
while temp>0:
    r1 = temp% 10 
    fact = 1
    for i in range (1,r1+1):
        fact *=i 
    sum += fact
    temp = temp//10

if (sum == num):
    print("Strong")
else:
    print("Not Strong")