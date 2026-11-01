# 3.7 Shrinking Guest List
guests = ['Barbara Sprouse', 'Giselle Bundchen', 'Elsa Hosk',
          'Bella Hadid', 'Anok Yai', 'Heidi Klum']

print("Sorry, my new dinner table won't arrive in time.")
print("I can only invite two people to dinner.\n")

# Pop guests one at a time until only two remain.
uninvited = guests.pop()
print(f"{uninvited.title()}, I'm sorry, I can't invite you to dinner.")
uninvited = guests.pop()
print(f"{uninvited.title()}, I'm sorry, I can't invite you to dinner.")
uninvited = guests.pop()
print(f"{uninvited.title()}, I'm sorry, I can't invite you to dinner.")
uninvited = guests.pop()
print(f"{uninvited.title()}, I'm sorry, I can't invite you to dinner.")

# The two remaining guests are still invited.
print(f"\n{guests[0].title()}, you are still invited to dinner!")
print(f"{guests[1].title()}, you are still invited to dinner!")

# Remove the last two names, leaving an empty list.
del guests[1]
del guests[0]
print(f"\nGuest list at the end: {guests}")