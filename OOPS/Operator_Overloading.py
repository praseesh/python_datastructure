class Add:
    def __init__(self, model, price):
        self.name = model
        self.price = price
    
    def __add__(self, other):
        output = self.price+ other.price
        print("Price of two Phones: ",output)
phone1 = Add("iPhone ", 50000)
phone2 = Add("Samsung ", 60000)
phone1+phone2

