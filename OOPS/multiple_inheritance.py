# class First:
#     def display_first(self):
#         print("First")
        
# class Second:
#     def display_second(self):
#         print("Second")
        
# class Third(First,Second):
#     def display_third(self):
#         print("Third")    

# x = Third()
# x.display_first()


# -----------------------------------------------------------------------------


class First:
    def display(self):
        print("First")
        
class Second:
    def display(self):
        print("Second")
        
class Third(First,Second):
    def display_third(self):
        print("Third")    

x = Third()
x.display()

print(Third.mro())
