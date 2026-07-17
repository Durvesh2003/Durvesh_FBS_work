# Structure 
di = {1:"Python", 2:"Java" , 3:"Testing"}

# 2.Hetrogeneous

di = {'id':101 , 'name':'ABC' , 5:45000.37}

# 3. ordered

# 4. element = mutable

di[6] = 34344
di[5] = 50000

print(di)

# 5. key are unique but values are duplicate

di = {1:'Python' , 2:'Java' , 2:'c'}          # override occurs
print(di)




d1 = {'id':101,'name': "Durvesh",'age': 20}
# print(d1.clear())

# d2 = d1.copy()
# print(d2)

# print(d1.get('id'))
# print(d1.get('ids','key not found'))
# print(d1.get('idss'))

# print(d1.items())

# print(d1.keys())

# print(d1.pop('id'))

# print(d1.popitem())

d1.update({'salary': 50000 , 'add': 'Panvel'})
print(d1)

print(d1.values())
