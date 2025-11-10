#sets are unique values

unique_numbers = {1, 2, 3, 2, 1,69,-1}

print("Original set:", unique_numbers)

unique_numbers.add(7)
print("After adding 7:", unique_numbers)

sorted_numbers = sorted(unique_numbers)
print("Sorted set as list:", sorted_numbers)