# Explicit Type Conversion

num_int = 123
num_str = "456"

# Explicitly converting num_str to an integer
num_str_int = int(num_str)

total = num_int + num_str_int

print("Total:", total)
print("Type of total:", type(total))



# Implicit type conversion

num_int = 123
num_float = 1.23

# Python automatically converts integer to float
total = num_int + num_float

print("Total:", total)
print("Type of total:", type(total))
