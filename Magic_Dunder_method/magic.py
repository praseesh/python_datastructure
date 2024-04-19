class Author:
    def __init__(self, name,book_name, pages):
        self.name = name
        self.book_name = book_name
        self.pages = pages
        # print("hiii")
    def __len__(self):
        print("hiii")
        return self.pages
        
    # def __str__(self) :
    #     print("hiii")
    #     return f"My name is {self.name} and {self.book_name} have {self.pages} Pages"
    def magic(s):
        """amgic docs"""
        print(s.name)
        print("magic print")
        
    
auth1 = Author("Paulo Coelho", "Alchemist", 372)
# print(len(auth1))
# print(auth1)
# auth1.magic()
print(auth1.magic.__doc__)

