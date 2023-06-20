# searches the target string for a given substring and returns indicies (returns -1 of not found)

s = "foobar".find('b')

print(s)  # -> 3 

s2 = "foobar".find('oob', 0, 1)

print(s2)  # -> -1