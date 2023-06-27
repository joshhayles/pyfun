# functions can be passed as arguments to other functions, returned as values from other functions, or assigned to variables and stored in data structures

def myfunc(a, b):
    return a + b

funcs = [myfunc]  # this creates a list called "funcs" and has a single element, myfunc (which is the function)

funcs[0]  # this retrieves the first element in the funcs list (which is myfunc)

print(funcs[0](2, 3))  # -> 5 
# this calls the function, passing 2 and 3 as arguments 