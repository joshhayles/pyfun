# create a global variable inside a function 

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)  # -> Python is fantastic

# you can also use the "global" keyword to change the value of another variable
