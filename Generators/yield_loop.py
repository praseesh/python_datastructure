def gen1():
    for i in range(10):
        yield i
        print(i)

for value in gen1():
    print(f"Yielded: {value}")


gen = gen1()  # Create a generator object

print(next(gen))  # This fetches the first yielded value, which is 0
# It will stop executing right after yielding, so the print statement inside gen1() hasn't run yet for 0.

print(next(gen))  # Now, when calling next() again, it first executes the print(i) for i=0, then yields 1.

print(next(gen))  # Now, when calling next() again, it first executes the print(i) for i=0, then yields 1.
