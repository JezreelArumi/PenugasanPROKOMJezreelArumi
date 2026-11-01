# 4.10 Slices
# Based on the cubes program from Exercise 4.8.
cubes = [value ** 3 for value in range(1, 11)]

print("The first three items in the list are:")
print(cubes[:3])

print("\nThree items from the middle of the list are:")
print(cubes[3:6])

print("\nThe last three items in the list are:")
print(cubes[-3:])