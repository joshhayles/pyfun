# identical to .find() - searches the target string for a given substring - but it will raise an exception if <sub> is not found:

s = "foobar".index('oob', 0, 1)

print(s)  # -> ValueError: substring not found
