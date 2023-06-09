# a built-in function used to create an empty set or convert an iterable (like a list or tuple) into a set. It removes duplicates and returns the unique elements in sorted order

my_list = [3, 3, 2, 4, 5, 3, 6]
my_set = set(my_list)

print(my_set)  # -> {2, 3, 4, 5, 6}
