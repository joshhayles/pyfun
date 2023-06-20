# determines whether the target string ends with the specified <suffix> and False otherwise

s = "foobar".endswith('arr')  

print(s)  # -> False

s2 = "foobar".endswith('bar')

print(s2)  # -> True

# comparison is restricted to the substring indicated by <start> and <end> options

s3 = "foobar".endswith('bar', 0, 2)

print(s3)  # -> False