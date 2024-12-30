class Counter:
    
    def __init__(self):
        self.value = 1
        
    def counter_up(self):
        self.value += 1
        
    def counter_down(self):
        self.value -= 1
        
    def __str__(self):
        return f"Count: {self.value}"
    
    def __add__(self,other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception("Invalid type")
        
counter1 = Counter()
counter2 = Counter()

counter1.counter_up()
counter2.counter_up()
counter2.counter_up()

print(counter1, counter2)
print(counter1 + counter2)