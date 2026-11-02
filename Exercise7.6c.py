# 7.6 Three Exits (c) (Tiga Cara Keluar): pernyataan break menghentikan loop
pesan_prompt = "\nBerapa usia Anda?"
pesan_prompt += "\nKetik 'keluar' jika sudah selesai. "

while True:
    usia = input(pesan_prompt)

    if usia == 'keluar':
        break

    usia = int(usia)
    if usia < 3:
        print("Tiket Anda gratis.")
    elif usia <= 12:
        print("Tiket Anda Rp 10.000.")
    else:
        print("Tiket Anda Rp 15.000.")