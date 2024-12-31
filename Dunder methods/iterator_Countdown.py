class Countdown:
    def __init__(self,start):
        self.current = start
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >=0 :
            value = self.current
            self.current -= 1
            return value
        else:
            raise StopIteration
for num in Countdown(5):
    print(num)