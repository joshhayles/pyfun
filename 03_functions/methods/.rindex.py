# identical to .rfind() but it will return an exception if not found:

s = "foo bar foo baz foo qux".rindex('zoo')

print(s)  # -> ValueError: substring not found
