# without arguments it splits a string into a list of substrings delimited by any sequence of whitespace and returns the substrings as a list

string = "foo   bar     res ting"

print(string.rsplit())  # -> ['foo', 'bar', 'res', 'ting']

# if a <sep> is specified, it's used as the delimiter for splitting:

string_2 = "new foo is rest ing"

print(string_2.rsplit(sep='s'))  # -> ['new foo i', ' re', 't ing']

# also see .split() where if <maxsplit> is specified, splits are counted from the left end of the string rather than the right