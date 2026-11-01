# 4.13 Buffet (a): the main program
# A tuple holds the five basic foods. Tuples can't be changed.
foods = ('soup', 'salad', 'rice', 'chicken', 'cake')

print("The original menu:")
for food in foods:
    print(food)

# The restaurant changes its menu: rewrite the whole tuple.
foods = ('soup', 'salad', 'pasta', 'chicken', 'ice cream')

print("\nThe revised menu:")
for food in foods:
    print(food)