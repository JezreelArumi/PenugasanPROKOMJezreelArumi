# 7.8 Deli (Toko Roti Lapis)
pesanan_sandwich = ['tuna', 'kalkun', 'sayur', 'ham']
sandwich_selesai = []

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Sandwich {sandwich_saat_ini} Anda sudah jadi.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nSandwich yang sudah dibuat:")
for sandwich in sandwich_selesai:
    print(f"- {sandwich.title()}")