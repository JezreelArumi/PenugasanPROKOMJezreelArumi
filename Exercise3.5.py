# 3.5 Changing Guest List
guests = ['Barbara Sprouse', 'Adriana Lima', 'Elsa Hosk']

print("--- First set of invitations ---")
print(f"{guests[0].title()}, I would love for you to join me for dinner.")
print(f"{guests[1].title()}, I would love for you to join me for dinner.")
print(f"{guests[2].title()}, I would love for you to join me for dinner.")

# One guest can't make it.
cant_attend = guests[1]
print(f"\n{cant_attend.title()} can't make it to dinner.")

# Replace that guest with a new person.
guests[1] = 'Giselle Bundchen'

print("\n--- Second set of invitations ---")
print(f"{guests[0].title()}, I would love for you to join me for dinner.")
print(f"{guests[1].title()}, I would love for you to join me for dinner.")
print(f"{guests[2].title()}, I would love for you to join me for dinner.")