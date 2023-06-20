# counts occurances of a substring in the target string

s = "foo goo moo".count('oo')

print(s)  # -> 3

# the count is restricted to the number of occurances within the substring when using <start> and <end> options:

s2 = "foo goo moo".count('oo', 2, 8)

print(s2)  # -> 1
