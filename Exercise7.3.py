# 7.3 Multiples of Ten (Kelipatan Sepuluh)
angka = input("Masukkan sebuah angka, saya cek apakah kelipatan 10: ")
angka = int(angka)

if angka % 10 == 0:
    print(f"\nAngka {angka} adalah kelipatan 10.")
else:
    print(f"\nAngka {angka} bukan kelipatan 10.")