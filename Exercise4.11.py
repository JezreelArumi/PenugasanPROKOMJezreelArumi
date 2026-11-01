# 4.11 My Pastas, Your Pastas
pastas = ['Macaroni', 'Fettucini', 'Fusilli']

# Copy the list with a slice, so there are two separate lists.
friend_pastas = pastas[:]

pastas.append('extra cheese')
friend_pastas.append('black pepper')

print("My favorite pastas are:")
for pasta in pastas:
    print(pasta)

print("\nMy friend's favorite pastas are:")
for pasta in friend_pastas:
    print(pasta)