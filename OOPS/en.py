class Student:
    def __init__(self, name, age, grade):
        self._name = name  # Protected attribute
        self._age = age    # Protected attribute
        self._grade = grade  # Protected attribute
    
    # Getter method
    def get_name(self):
        return self._name
    
    # Setter method
    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self._grade = grade

# Create a Student object
student1 = Student("Alice", 18, 90)

# Accessing attributes through methods
print(student1.get_name())  # Output: "Alice"

# Modifying attributes through methods
student1.set_grade(95)