from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def __init__(self, brand, price,sunroof):
        super().__init__(brand, price)
        self.sunroof = sunroof
    def stop(self):
        print("Car stopped")

c1 = Car("BMW",5000000,"Yes")
c1.stop()
