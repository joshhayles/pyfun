# "is" a comparison operator used to check if two variables refer to the same object in memory. It checks for object identity, not object equality regarding the elements of the object:

a = [1, 2, 3]
b = a

print(a is b)  # -> True (the variables point to the same object)


# "==" evaluates to True if the objects referred to by the variables are equal (i.e. have the same elements)

c = list(a)

print(a == c)  # -> True (elements are the same)


# In the following scenario, although the elements of 'a' and 'c' are the same, they are two separate list objects stored in different memory locations:

print(a is c)  # -> False (objects are stored in different memory locations)