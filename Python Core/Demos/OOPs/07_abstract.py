from abc import ABC , abstractmethod
class Emp(ABC):
    def __init__(self,id,name,sal):
        self.id = id
        self.name = name
        self.sal = sal
    @abstractmethod
    def calSal(self):
        pass

class Teacher(Emp):
    def __init__(self, id, name, sal,incentive):
        super().__init__(id, name, sal)
        self.incentive = incentive
    def calSal(self):
        print(f"Total Sal {self.sal+ self.incentive}")

e1 = Teacher(18,"Virat",100000,150)
e1.calSal()