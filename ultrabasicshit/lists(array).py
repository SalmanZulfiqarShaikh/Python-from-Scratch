grocerries = ["eggs", "milk", "butter", "bread", "apples"]

print(grocerries)

print("First item:", grocerries[0]) #accessing first item

grocerries.append("bananas")

print("After appending bananas:", grocerries)

grocerries.remove("milk")
print("After removing milk:", grocerries)

print("Length of the list:", len(grocerries))
grocerries.sort()
print("Sorted list:", grocerries)