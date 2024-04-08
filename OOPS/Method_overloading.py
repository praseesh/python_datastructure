class A:
    def func(self):
        print("Function in Class A")
        
class B(A):
    def func(self):
        super().func()
        print("Function in Class B")
        
obj = B()
obj.func()