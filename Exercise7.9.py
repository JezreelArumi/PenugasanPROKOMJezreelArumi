# 7.9 No Pastrami (Tanpa Pastrami)
pesanan_sandwich = ['pastrami', 'tuna', 'pastrami', 'kalkun', 'sayur',
                    'pastrami', 'ham']
sandwich_selesai = []

print("Pastrami di toko ini sudah habis.")
while 'pastrami' in pesanan_sandwich:
    pesanan_sandwich.remove('pastrami')

print(f"Pesanan yang tersisa: {pesanan_sandwich}\n")

while pesanan_sandwich:
    sandwich_saat_ini = pesanan_sandwich.pop()
    print(f"Sandwich {sandwich_saat_ini} Anda sudah jadi.")
    sandwich_selesai.append(sandwich_saat_ini)

print("\nSandwich yang sudah dibuat:")
for sandwich in sandwich_selesai:
    print(f"- {sandwich.title()}")