def myFun(arg1, **kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun("Hi", first='Geeks', mid='for', last='Geeks')


def print_info(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_info(name="Alice", age=30, city="New York")


# def greet(name, age):
#     print(f"Hello, {name}. You are {age} years old.")

# data = ["Alice", 30]
# greet(*data)  # Unpacking list into positional arguments

# data = {"name": "Bob", "age": 25}
# greet(**data)  # Unpacking dictionary into keyword arguments

