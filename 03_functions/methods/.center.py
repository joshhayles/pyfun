# centers a string in a field:
# center(width, fill) | fill character can only be one character long

s = "foo".center(10)

print(s)  # ->   '       foo          '

s2 = "foo".center(5, '+')

print(s2)  # -> +foo+
