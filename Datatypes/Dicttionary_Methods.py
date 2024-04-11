# Clear()

# my_dict = {
#     'name': 'John',
#     'age': 30,
#     'city': 'New York'
# }
# my_dict.clear()
# print(my_dict)

# Copy()

# original_dict = {
#     'name': 'John',
#     'age': 30, 
#     'city': 'New York'
#     }
# copied_dict = original_dict.copy()
# copied_dict["Country"] = "USA"
# original_dict["age"] = 20
# print(f"Copied Dictionary: {copied_dict}\n\nOriginal Dictionary: {original_dict}")

# FromKeys()

list1 = ("name", "age", "city")
# values = "unknown"
new_dict = dict.fromkeys(list1)
print(new_dict)

# Get()

# my_dict = {
#     'name': 'John', 
#     'age': 30, 
#     'city': 'New York'
# }

# n = my_dict.get("name")
# a = my_dict.get("gender","Not to say")

# print(f"Name: {n}\nAge :{a}")

# Items()

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# items = my_dict.items()
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

# Keys()

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# keys = my_dict.keys()
# for key in keys:
#     print(key)

# Value()

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# values = my_dict.values()
# for value in values:
#     print(value)

# Pop()
# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# removed_value = my_dict.pop('age')
# print("Removed value:", removed_value)
# print("Updated dictionary:", my_dict) 

# PopOut()

# my_dict = {'name': 'John', 'age': 30,"Phno": 9877, 'city': 'New York',"gender" : "Male"}
# removed_item = my_dict.popitem()

# print("Removed item:", removed_item)  
# print("Updated dictionary:", my_dict)

# SetDefault()

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# name = my_dict.setdefault('name', 'Jacob')
# gender = my_dict.setdefault('gender', 'Unknown')

# print("Name:", name) 
# print("Gender:", gender) 
# print("Updated dictionary:", my_dict)


# Update()

# my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
# additional_info = {'gender': 'Male', 'occupation': 'Engineer'}

# my_dict.update(additional_info)

# print("Updated dictionary:", my_dict)


# 9645096072 govindan