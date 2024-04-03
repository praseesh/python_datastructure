def upper_func(func):
    def inner_func(name):
        result = func(name)
        return result.upper()
    return inner_func

@upper_func
def hello(name):
    return "Hello " + name

print(hello("Praseesh"))