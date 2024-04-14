def square_list():
    for i in range(1, 5):
        yield i**2
        
x = square_list()

for i in x:
    print(i)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
