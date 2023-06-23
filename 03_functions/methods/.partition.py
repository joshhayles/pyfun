# s.partition separates a string into three parts, based on the delimiter. The tuple contains the part of the string before the delimiter, the delimiter itself, and the part after the delimiter

string = "josh"

print(string.partition('o'))  # -> ('j', 'o', 'sh')

# there is also s.rpartition(<sep>) - string is split at the last occurence of the delimiter