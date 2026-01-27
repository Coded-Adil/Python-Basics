# Using args to multiple parameters in a function

def addition(*args): # args is a tuple. multiple arguments can be passed
    result = sum(args)
    print(args)
    return result

r = addition(12, 10, 2, 18, 10)
print(r)