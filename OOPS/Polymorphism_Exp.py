class Pets:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self,sound):
        print(f"The animal sound is {sound}")
        
class Cat(Pets):
    
    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    # def make_sound(self):
    #     print("Meow")


class Dog(Pets):

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    # def make_sound(self):
    #     print("Bark")

cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

# for animal in (cat1, dog1):
cat1.make_sound("grrr")
cat1.info()


dog1.make_sound("BOWWW")
dog1.info()

