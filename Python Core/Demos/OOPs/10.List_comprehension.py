li1 = [ele for ele in range(1,11)]

print(li1)

li2 = [ele for ele in range(1,11) if ele % 2 == 0]

print(li2)

# Nested List Comprehension

li = [[ele for ele in range(i * 10 + 1 , i * 10 + 11)] for i in range(0,10) ]

print(li)

# Dictionary Comprehension 

di = { n : n**2 for n in range(1,11)}
print(di)