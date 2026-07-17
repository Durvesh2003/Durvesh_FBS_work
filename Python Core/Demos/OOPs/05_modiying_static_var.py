class Student:
    count = 0
    def __init__(self,roll_no,name,age):
        Student.count += 1
        self.rn = roll_no
        self.nm = name
        self.age = age

    def getData(self):
        print(self.rn)
        print(self.nm)
        print(self.age)

    def totalCount():
        return Student.count

obj1 = Student(20,'Prasad',21)
obj2 = Student(21,"pranav",23)
obj1 = Student(23,'Pranv',21)

print(Student.totalCount())