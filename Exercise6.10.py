# 6.10 Favorite Numbers (modified from Exercise 6.2)
favorite_numbers = {
    'jokowi': [7, 14],
    'anies': [42],
    'prabowo': [3, 9, 27],
    'anies': [11, 22],
    'teddy': [9, 99],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")