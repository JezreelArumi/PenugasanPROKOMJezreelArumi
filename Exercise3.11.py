# 3.11 Intentional Error (a): this version produces an IndexError
# The list has three items (indexes 0, 1, 2), so index 3 doesn't exist.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])

# 3.11 Intentional Error (b): the corrected version
# The last item of a three-item list is at index 2 (or -1).
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[2])
print(motorcycles[-1])