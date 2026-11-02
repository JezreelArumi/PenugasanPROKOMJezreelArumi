# 6.8 Pets
pet_0 = {'kind': 'dog', 'owner': 'maria'}
pet_1 = {'kind': 'cat', 'owner': 'chen'}
pet_2 = {'kind': 'goldfish', 'owner': 'sofia'}
pet_3 = {'kind': 'rabbit', 'owner': 'jaden'}

pets = [pet_0, pet_1, pet_2, pet_3]

for pet in pets:
    print(f"\nKind of animal: {pet['kind']}")
    print(f"Owner: {pet['owner'].title()}")