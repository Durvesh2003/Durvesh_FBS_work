s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = {50,60}
s4 = {70,80}

print(type(s1))

# s1[0] = 30      # error

# s1.add(100)

# s1.clear()

# s2 = s1.copy()
# print(s1)
# print(s2)

res = s1.difference(s2)
# s1.difference_update(s2)
# print(s1)

res = s1.intersection(s2)
# s1.intersection_update(s2)
# print(s1)
res = s1.union(s2)
res = s1.symmetric_difference(s2)
res = s2.issuperset(s3)
res = s2.issubset(s3)
res = s3.issuperset(s2)


# s1.discard(40)
# print(s1)

print(res)

# res = s1.isdisjoint(s4)
# print(res)

# s1.pop()
# print(s1)

s1.symmetric_difference_update(s2)
print(s1)  

# s1.add({1,2,3,4})
# print(s1)                 error 

s1.add((1,2,3,4))
print(s1)
