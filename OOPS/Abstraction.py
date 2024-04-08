from abc import ABC, abstractmethod
class Vehicle(ABC):
    def start_engine(self):
        print ("Engine starting")
    
    @abstractmethod
    def gear(self):
        pass
    
class Car(Vehicle):
    def music(self):
        print("playing music")
    
    def gear(self):
        print("Gear changed Automatically")
        
class Bike(Vehicle):
    def helmet(self):
        print("wearing helmet")
    def gear(self):
        print("Gear changed Manually")
        
bike1 = Bike()
car1 = Car()

car1.gear()
bike1.gear()