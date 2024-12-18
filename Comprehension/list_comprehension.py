animals = ["Lion", "Tiger", "Monkey", "Elephant", "Frog"]
filtered_animals = []
for animal in animals:
    filtered_animals.append(animal.title())

print(filtered_animals)


filtered_animal = [animal for animal in animals]
print(filtered_animal)

# a,b,c = [1,2,3]

# print(f"a:{a}\nb:{b}\nc:{c}")

a,_,c = [1,2,3]

print(f"a:{a}\nb:{_}\nc:{c}")