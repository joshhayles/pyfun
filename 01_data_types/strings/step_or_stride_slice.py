# adding an additional : and a third index designates a stride (also called step), which indicates how many characters to jump after retrieving each character in the slice

# skipping every other character:

s = "foobar"

print(s[0:6:2])  # -> foa

# you can also omit the first and second indicies, and default to the first and last characters:

s2 = "123" * 5

print(s2[::2])  # -> 13213213

# start at the last character and step backward by 2, up to but not including the first character:

s3 = "foosball"

print(s3[7:0:-2])  # -> laso

# a more intuitive form would be to omit the first and second indicies. This way, the defaults are reversed: the first index defaults to the end of the string, and the second index defaults to the beginning:

print(s3[::-2])  # -> laso

# you can reverse an entire sentence like this:

s4 = "Hello, Joshua!"
print(s4[::-1])  # -> !auhsoJ ,olleH