# iterating over a dictionary and accessing an element using square brackets ( [] ) retrieves the value associated with that key:

from collections import Counter

string = "jjoshuaaa"
count = {}

for char in string:
    if char not in count:
        count[char] = 0

    count[char] += 1
        
for key, value in count.items():
    print(key, ":", value)

"""
j : 2
o : 1
s : 1
h : 1
u : 1
a : 3
"""

# printing just the values:

for value in count.values():
    print(value)

# printing just the keys:

for key in count.keys():
    print(key)