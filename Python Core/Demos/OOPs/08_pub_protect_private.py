class Emp:
    def __init__(self,id,name,salary):
        self.id = id
        self._name = name
        self.__sal = salary

e1 = Emp(101,"Durvesh",1000000)
print(e1.id)
print(e1._name)
# print(e1__sal)       # since it is private we cannot access it outside 
print(e1._Emp__sal)  # Naming convention to access private
