# returns an iterator of tuples with the index and value pairs from an iterable

# Example: create a function that returns a list of indicies where the elements of the input list are even:

def find_even_indicies(numbers):
    even_indicies = []

    for index, num in enumerate(numbers):
        if num % 2 == 0:
            even_indicies.append(index)

    return even_indicies

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
even_indicies = find_even_indicies(my_list)

print(even_indicies)  # [1, 3, 5, 7]
