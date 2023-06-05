# string slicing

# if you omit the first index, the slice starts at the beginning:

s = "foobar"

print(s[:4])  # -> foob

# if you omit the second index, it will slice through to the end of the string:

print(s[1:])  # -> oobar

# that's the same as: print(s[1:len(s)])

################################################

s2 = "foobar"
slice = s2[:3] + s2[3:]
# slice from the beginning, up to but not including index 3. Then, slice from index 3 to the end of the string.

print(slice)  # -> foobar

# compare the slices to see if they are equal:
print(s2[:3] + s2[3:] == s2)  # -> True

# you can also omit both indicies to return the original string (not a copy):

a = "foobar"
b = s[:]

print(id(a))  # -> 4533470256
print(id(b))  # -> 4533470256
print(a is b)  # -> True