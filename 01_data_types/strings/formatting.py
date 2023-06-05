# format a result (i.e. 1000) to look like 1,000

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}") # -> 3,002

# determine the number of digits you want to print

x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y)

print(f"{z:.2f}")  # -> 1.00
