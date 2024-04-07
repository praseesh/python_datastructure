class DangerBoys:
    year = 2024
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
       
    def display(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Place: {self.place}")
        
    def add_age(self):
        self.age = self.age + 1
       
    def relocate(self, place):
        self.place = place
    @classmethod 
    def add_year(cls):
        cls.year = cls.year + 1
        
       
person_1 = DangerBoys("John", 34, "Tokyo")
person_2 = DangerBoys("Jacob", 55, "New York")
person_1.add_age()
person_2.add_age()
person_1.display()
person_1.relocate("Canada")
person_1.display()
person_2.display()

DangerBoys.add_year()

person_1.display()
person_2.display()