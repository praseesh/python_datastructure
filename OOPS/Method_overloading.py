class A:
    def func(self, name ,age):
        print("Function in Class A")
    
    def func(self, name ,age,adr):
        print("Function in dsfdfd A")
        
class B(A):
    def func(self,name):
        super().func( name,8)
        print("Function in Class B")
        
obj = B()
obj.func("sas")