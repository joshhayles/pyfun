# represents complex numbers (consists of 'real' and 'imaginary')

# example

x = 3 + 2j
real_part = x.real 
imaginary_part = x.imag 
conjugate = x.conjugate()

print(real_part)  # -> 3.0
print(imaginary_part)  # -> 2.0
print(conjugate)  # -> (3-2j)

# a conjugate of a complex number is another complex number that has the same real part but the opposite sign for the imaginary part
    # example
    # a + bj where 'a' is the real part and 'b' is the imaginary part, the conjugate is a - bj (changing the sign)
