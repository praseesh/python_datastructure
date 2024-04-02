
def upper_func(func):
    def inner_func(name):
        result = func(name)
        return result
    return inner_func


def hello(name):
    return "Hello " + name

f = upper_func(hello)
print(f("Praseesh"))