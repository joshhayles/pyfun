# methods for removing whitespaces 

# .rstrip() - removes whitespace from the right side of string
# .lstrip() - removes whitespace from the left side of string
# .strip() - removes whitespace from both the left and right side

name = "Joshua  "

print(name.rstrip())  # -> Joshua

name2 = "  Joshua"

print(name2.lstrip())  # -> Joshua

name3 = "   Joshua    "

print(name3.strip())  # -> Joshua
