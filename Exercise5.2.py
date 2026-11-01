# 5.2 More Conditional Tests
# Each category has at least one True and one False result.

print("--- Equality and inequality with strings ---")
pet = 'dog'
print(pet == 'dog')     # True
print(pet == 'cat')     # False
print(pet != 'cat')     # True
print(pet != 'dog')     # False

print("\n--- Tests using the lower() method ---")
car = 'Audi'
print(car.lower() == 'audi')    # True
print(car.lower() == 'bmw')     # False
print(car == 'audi')            # False, because case matters here

print("\n--- Numerical tests ---")
age = 19
print(age == 19)    # equal: True
print(age == 21)    # equal: False
print(age != 21)    # not equal: True
print(age != 19)    # not equal: False
print(age < 21)     # less than: True
print(age < 18)     # less than: False
print(age > 18)     # greater than: True
print(age > 19)     # greater than: False
print(age <= 19)    # less than or equal: True
print(age <= 18)    # less than or equal: False
print(age >= 19)    # greater than or equal: True
print(age >= 20)    # greater than or equal: False

print("\n--- Tests using and, or ---")
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 18)   # True and True -> True
print(age_0 >= 21 and age_1 >= 21)   # True and False -> False
print(age_0 >= 21 or age_1 >= 21)    # True or False -> True
print(age_0 < 21 or age_1 >= 21)     # False or False -> False

print("\n--- Is an item in a list? ---")
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)   # True
print('pepperoni' in requested_toppings)   # False

print("\n--- Is an item not in a list? ---")
print('pepperoni' not in requested_toppings)   # True
print('onions' not in requested_toppings)      # False