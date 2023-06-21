# replaces each tab character with spaces. Be default, spaces are filled assuming a tab stop at every eighth column

s = "a\tb\tc".expandtabs(4)  # empty argument defaults to 8

print(s)  # -> a    b    c