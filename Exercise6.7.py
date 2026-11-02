# 6.7 People
person_0 = {
    'first_name': 'Joko',
    'last_name': 'Widodo',
    'age': 65,
    'city': 'Surakarta',
}
person_1 = {
    'first_name': 'Ganjar',
    'last_name': 'Pranowo',
    'age': 58,
    'city': 'Semarang',
}
person_2 = {
    'first_name': 'Anies',
    'last_name': 'Baswedan',
    'age': 57,
    'city': 'Jakarta',
}

people = [person_0, person_1, person_2]

for person in people:
    print(f"\nFirst name: {person['first_name'].title()}")
    print(f"Last name: {person['last_name'].title()}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city'].title()}")