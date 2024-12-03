class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method for name
    def get_name(self):
        return self._name

    # Setter method for name
    def set_name(self, name):
        self._name = name

    # Getter method for age
    def get_age(self):
        return self._age

    # Setter method for age
    def set_age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self._age = age

# Creating an instance of Person
person = Person("Alice", 30)

# Accessing attributes using getter methods
print("Name:", person.get_name())
print("Age:", person.get_age())

# Using setter methods to change attributes
person.set_name("Bob")
person.set_age(55)

# Accessing attributes again to see changes
print("Name:", person.get_name())
print("Age:", person.get_age())
