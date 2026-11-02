# 7.6 Three Exits (b) (Tiga Cara Keluar): variabel aktif mengatur perulangan
pesan_prompt = "\nBerapa usia Anda?"
pesan_prompt += "\nKetik 'keluar' jika sudah selesai. "

aktif = True
while aktif:
    usia = input(pesan_prompt)

    if usia == 'keluar':
        aktif = False
    else:
        usia = int(usia)
        if usia < 3:
            print("Tiket Anda gratis.")
        elif usia <= 12:
            print("Tiket Anda Rp 10.000.")
        else:
            print("Tiket Anda Rp 15.000.")