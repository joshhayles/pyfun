# lambda is an anonymous function in Python that has a single expression evaluated when the function is called: lambda [parameters]: expression

# this is a way of creating one-line functions without explicitly defining them using "def" keyword

# "lambda" is a keyword that indicates the start of the function
# [parameters] refer to the input parameters of the function (optional)
# : expression is the operation that the lambda function will evaluate and return its result

# Example: using lambda for one-line function creation inside of another function:

def call_dictionary(operator, x, y):
    return {
        "add": lambda: x + y,
        "subtract": lambda: x - y
    }.get(operator, lambda: None) ()

print(call_dictionary("add", 2, 2))  # -> 4
print(call_dictionary("subtract", 2, 2))  # -> 0
print(call_dictionary("divide", 2, 2))  # -> None

# line 12 starts the return of a dictionary
# line 13 defines the key: value pair in the dictionary. The key is "add" and the value is the lambda function that returns the sum of x + y
# line 14 does the same as line 13, except it will subtract x from y
# line 15 uses .get() method to retrieve the operator arguments (which are the keys: "add" and "subtract"), which will return the corresponding values of the keys (i.e. the lambda functions) if the key is present in the dictionary. Otherwise, it will return the default value of None (i.e. lambda: None). When you pass "add" as the operator argument to the call_dictionary function, it retrieves lambda: x + y from the dictionary, then immediately calls that lambda function by appending () at the end. The same happens with "subtract"