class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"

my_car = Car('Toyota', 'Corolla', 2021)
my_car2 = Car("BMW", "Q7",2018)

print(str(my_car))   
print(repr(my_car))   
print(str(my_car2))  
print(repr(my_car2))  
