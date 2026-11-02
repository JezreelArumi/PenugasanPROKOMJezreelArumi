# 7.6 Three Exits (a) (Tiga Cara Keluar): tes kondisi di pernyataan while
pesan_prompt = "\nBerapa usia Anda?"
pesan_prompt += "\nKetik 'keluar' jika sudah selesai. "

usia = ""
while usia != 'keluar':
    usia = input(pesan_prompt)

    if usia != 'keluar':
        usia = int(usia)
        if usia < 3:
            print("Tiket Anda gratis.")
        elif usia <= 12:
            print("Tiket Anda Rp 10.000.")
        else:
            print("Tiket Anda Rp 15.000.")