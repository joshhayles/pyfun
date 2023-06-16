# To iterate over the indices of a sequence, you can combine range() and len() as follows:

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print(i, a[i])


# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb


#  You can do the same thing using enumerate():

b = ['Mary', 'had', 'a', 'little', 'lamb']

for index, item in enumerate(b):
    print(index, item)


# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb
