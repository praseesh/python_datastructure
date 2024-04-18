# Creating a Dictionary

new_dict1 = {
    "Rahul" : 1234,
    "Sooraj" : 4567,
    "Rohan" : 4321
}
"""
# Accessing the Values

a = new_dict1["Sooraj"]
print(a)
print(new_dict1["Rahul"])

# Modifying the Dictionary

new_dict1["Rohan"] = "New value"

new_dict1["Kumar"] = "Newly added"

print(f"Modified Dictionary: {new_dict1}")
"""

# a = new_dict1[0]
# print(a)

for key in new_dict1.keys():
    # if key == "Rohan":
        print(f"{key}")
