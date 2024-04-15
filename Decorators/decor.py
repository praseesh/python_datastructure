def upper_case(func):
    def inner(y):
        result = func(y)
        return result.upper()
    return inner

@upper_case
def hello(name):
    return "hello" +" " + name
    

print(hello("praseesh"))