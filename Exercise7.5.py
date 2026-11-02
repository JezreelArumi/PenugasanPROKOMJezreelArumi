# 7.5 Movie Tickets (Tiket Bioskop)
# Di bawah 3 tahun gratis, usia 3 sampai 12 tahun Rp 10.000,
# dan di atas 12 tahun Rp 15.000.
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