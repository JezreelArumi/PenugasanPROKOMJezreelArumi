# 4.15 Code Review (c): Exercise 4.13 reviewed against PEP 8
# Checked: four spaces per indent, lines under 80 characters, and
# a blank line only between the original and revised menus.
foods = ('soup', 'salad', 'rice', 'chicken', 'cake')

print("The original menu:")
for food in foods:
    print(food)

foods = ('soup', 'salad', 'pasta', 'chicken', 'ice cream')

print("\nThe revised menu:")
for food in foods:
    print(food)