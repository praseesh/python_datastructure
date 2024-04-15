def upper_func(func):
    def inner_func():
        result = func()
        return result.upper()
    return inner_func
@upper_func
def hello_name():
    name = "praseesh"
    return f"Good Morning { name}"

print(hello_name())


# f = upper_func(hello_name)
# print(f())

# print(upper_func(hello_name)())