def upper_case(functio):
    def inner(y):
        result = x(y)
        return result.upper()
    return inner

@upper_case
def hello():
    return "hello" + name
    

    hello("praseesh")