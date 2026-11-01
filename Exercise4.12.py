# 4.12 More Loops
# makanan
makanan_saya = ['rendang', 'betutu', 'soto']
makanan_teman = makanan_saya[:]

makanan_saya.append('ikan bakar')
makanan_teman.append('bakso')

print("Makanan favorit saya:")
for food in makanan_saya:
    print(food)

print("\nMakanan favorit teman saya:")
for food in makanan_teman:
    print(food)