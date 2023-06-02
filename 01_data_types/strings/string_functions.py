# Python provides many functions that are built-in to the interpreter and always available. Here are a few that work with strings:

# Given a numeric value n, chr(n) returns a string representing the character that corresponds to n:

print(chr(97))  # -> a

print(chr(35))  # -> #

# ord() does the opposite of chr() - it returns the integer value for a given character:

print(ord("a"))  # -> 97

print(ord("#"))  # -> 35

# These functions will return numeric values for Unicode characters as well
