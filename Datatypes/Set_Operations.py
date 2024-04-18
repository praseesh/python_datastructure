# set1 = set({})

# set1.add(6)
# print(set1)
# set1.update([33,22])
# print(set1)

s1= {"Apple", "Mango", "Orange"}
s2 = {"Red", "Orange", "Yellow"}

print(f"First:  {s1}\nSecond:  {s2}")
# if "Apple" in s1:
    # print("Apple")
"""Union"""

x = (s1|s2)
print(x)
x = s1.union(s2)
print(f"\nUnion:   {x}\n")

"""Intersection"""
y = s1.intersection(s2)
print(f"Intersection: {y}\n")
y = (s1&s2)



"""Difference"""
z = s1-s2
print(f"Difference: {z}\n")
z = s1.difference(s2)