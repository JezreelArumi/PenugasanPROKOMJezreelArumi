# 7.10 Dream Vacation (Liburan Impian)
tanggapan = {}
survei_aktif = True

while survei_aktif:
    nama = input("\nSiapa nama Anda? ")
    tempat = input("Jika bisa mengunjungi satu tempat di dunia, "
                   "ke mana Anda akan pergi? ")

    tanggapan[nama] = tempat

    ulangi = input("Apakah ada orang lain yang mau menjawab? (ya/tidak) ")
    if ulangi == 'tidak':
        survei_aktif = False

print("\n--- Hasil Survei ---")
for nama, tempat in tanggapan.items():
    print(f"{nama} ingin mengunjungi {tempat}.")