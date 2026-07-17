str = 'FirstBit Solutions'

res = str.capitalize()
res = str.count('bit')
res = str.endswith('ions')
res = str.find('Bit')
res = str.find('bit')
res = str.index('Bit')
res = str.isalnum()          #alpha or numeric
res = str.islower()
res = str.isspace()
res = str.split(' ')
res = str.replace('s','*')
res = str.startswith('First')
res = str.swapcase()
res = str.title()
res = str.upper()
print(res)

str4 = "['127.0.0.1']"
res3 = str4.strip("[']")
print(res3)


print(res)

str1 = 'first'
a = str1.isalpha()
print(a)

x= '12345678'
b = x.isdigit()
print(b)

str3 = 'Firsrbit solutions   '

count = 0
for char in str3:
    if char.isspace():    # if char == ' '    or directly str3.count(' ')
        count += 1
print(count)

li = ['a','b','c']
res1 = '_'.join(li)
print(res1)