class Student:
    def setData(self,roll_no,name,age):
        self.rn = roll_no
        self.nm = name
        self.age = age

    def getData(self):
        print(self.rn)
        print(self.nm)
        print(self.age)

obj1 = Student()
obj1.setData(20,'Prasad',21)

obj2 = Student()
obj2.setData(21,"pranav",23)

obj1.getData()
print("#######################")
obj2.getData()