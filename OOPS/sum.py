class Sum:
    def find_sum(self,a,b,c=None):
        if c == None:
            print(a+b)
        else:
            print(a+b+c)
a = Sum()

a.find_sum(4,6,6)
    