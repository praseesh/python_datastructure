class DangerBoys:
    
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
       
    def display(self):
        print(f"Name: {self.name}\n Age: {self.age}\n Place: {self.place}")
       
    def relocate(self, place):
        self.place = place
       
person_1 = DangerBoys("John", 34, "Tokyo")
person_2 = DangerBoys("Jacob", 55, "New York")

person_1.display()
person_1.relocate("Canada")
person_1.display()
