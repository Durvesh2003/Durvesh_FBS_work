li = [3,4,68,45,50,1]
l3 = [3,4,68,45,50,1]

# li.append(30)
# print(li)

# li.clear()
# print(li)

li1 = li.copy()
print(li)
print(f"Id li = {id(li)}")
print(f"Id li1 = {id(li1)}")

print(li.count(68))

print(li is l3)

print(li == l3)

li.extend([20,50])
print(li)

li.insert(1,7)
print(li)

li.pop(7)
print(li)

li.sort()
print(li)

li.sort(reverse=True)
print(li)

li.remove(1)
print(li)
