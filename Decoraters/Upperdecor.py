def upper_func(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

@upper_func
def hello(name):
    return "hi " + name

print(hello("Praseesh"))