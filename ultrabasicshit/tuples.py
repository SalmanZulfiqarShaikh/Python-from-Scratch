# tuples are immutable sequences, typically used to store collections of heterogeneous data

numbers = (1,2,3)

print("Original tuple:", numbers)

# accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])
# unpacking
a, b, c= numbers
print("Unpacked values:", a, b)
# concatenation
more_numbers = (4,5,6)
print("Concatenated tuple:", numbers + more_numbers)
# repetition
print("Repeated tuple:", numbers * 2)
# length
print("Length of the tuple:", len(numbers))

print("Is 2 in numbers?", 2 in numbers)
# iteration
for num in numbers:
    print("Tuple element:", num)
    # getting the typef)
print("Type of numbers:", type(numbers))