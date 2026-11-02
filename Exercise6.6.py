# 6.6 Polling
favorite_languages = {
    'jeva': 'python',
    'naila': 'c',
    'queena': 'rust',
    'al': 'python',
}

people = ['jeva', 'naila', 'queena', 'al', 'sarah']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you for responding to the poll, {person.title()}!")
    else:
        print(f"{person.title()}, please take our poll!")