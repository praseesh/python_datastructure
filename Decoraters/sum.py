# def outer(x):
#     def inner():
#         return x 
#     return inner

# add_five = outer(5,8)
# print(add_five)
# res = add_five(6)
# print(res)

# def dec():
#     return "this is a decorator"

# @dec
# def check():
#     return "this is check"

def dec(func):
    def wrapper():
        print("Before calling the function")
        result = func()
        print(result)
        print("After calling the function")
    print(wrapper)
    return wrapper


def deco(func):
    def wrapper():
        print("Before calling the 2nd function")
        result = func()
        print(result)
        print("After calling the 2nd function")
    print(wrapper)
    return wrapper

@dec
def check():
    print("hello")
    return "this is check"

# Now, when you call check(), it will be decorated by dec
print(check())

