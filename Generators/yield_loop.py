def gen1():
    for i in range(10):
        yield i
        # print(i)

# for value in gen1():
#     print(f"Yielded: {value}")

gen = gen1()  # Create a generator object
# print(next(gen))  # This fetches the first yielded value, which is 0

print(next(gen)) 
print(next(gen)) 
print(next(gen)) 