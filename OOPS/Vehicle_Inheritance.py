class Vehicle:
    def __init__(self, company, model, color, engine):
        self.company = company
        self.model = model
        self.color = color
        self.engine = engine
        
    def start_engine(self):
        print("Engine started..!!")
    
    def change_gear(self):
        print("gear changed..!!")
        
class Car(Vehicle):
    
    def __init__(self, company, model, color, engine, bodytype):
        super().__init__(company, model, color, engine)
        self.bodytype = bodytype
    
    def open_sunroof(self):
        print(f"{self.company} {self.model} Opening sunroof")
        
    def display(self):
        print(f"Company: {self.company}\nModel: {self.model}\nColor: {self.color}\nEngine: {self.engine}")
        
        
car1 = Car("Audi", "Q7", "Black", "Petrol","Metalic")
car1.display()
car1.open_sunroof()
