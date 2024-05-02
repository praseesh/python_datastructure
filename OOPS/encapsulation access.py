class Car:
    def __init__(self, make, model, year):
        self.__make = make  # private attribute
        self.model = model  # public attribute
        self.year = year  # public attribute

    def display_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

# Creating a Car object
my_car = Car("Toyota", "Corolla", 2022)

# Accessing public attributes directly
print(my_car.model)  # Output: Corolla
print(my_car.year)   # Output: 2022

# Accessing private attribute using getter method
print(my_car.display_make())  # Output: Toyota

# Trying to access private attribute directly (this will raise an error)
# print(my_car.__make)

# Updating private attribute using setter method
my_car.set_make("Honda")
print(my_car.display_make())  # Output: Honda
