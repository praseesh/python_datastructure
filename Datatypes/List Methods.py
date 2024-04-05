# my_list = [3, 1, 4, 1, 5, 9, 2]
# # Append a number

# my_list.append(6)
# print(my_list)

# # Append a List
# words = ["hello", "world", "python"]
# my_list.append(words)

# # Append list

# nums = [1,3,5,3]
# nums.append(my_list)
# print(f"Nums: {nums}")


# # Sorting

# nums.sort()
# print(f"Sorted: {nums}")

# # Reverse()
# nums.reverse()
# print(f"Reverse: {nums}")

# # Range in list

# another_list = list(range(95, 3, -5))
# print(another_list)


my_list = [3, 1, 4, 1, 5, 9, 2]

# # Index()

# index_of_2 = my_list.index(9)
# print("Index of 4:", index_of_2)

# Extend()

my_list.extend([7, 8])
print("After extend:", my_list)

# Copy()

copied_list = my_list.copy()
copied_list.append(5432424242)
print(f"Copied List: {copied_list}")

# Insert()

my_list.insert(2, "x")
print(f"After Inserting:{my_list}")

# Remove()
my_list.remove(8)
print("After remove:", my_list)

# Pop()
popped_item = my_list.pop()  # Removes and returns the last item
print("After pop:", my_list, "(Popped Item:", popped_item, ")")

# Count()

count_of_1 = my_list.count(1)
print("Count of 1:", count_of_1)