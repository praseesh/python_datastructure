def upper(func, name):
    result = func(name)
    return result

def name_func(name):
    return "Hello" + name

def good_morning(name):
    return "Good Morning" + name

print(upper(name_func, " Praseesh"))
print(upper(good_morning, " Praseesh"))