# 8.11 Archived Messages (Pesan Arsip)
def kirim_pesan(pesan_belum_terkirim, pesan_terkirim):
    """Cetak setiap pesan, lalu pindahkan ke daftar pesan terkirim."""
    while pesan_belum_terkirim:
        pesan_saat_ini = pesan_belum_terkirim.pop()
        print(f"Mengirim pesan: {pesan_saat_ini}")
        pesan_terkirim.append(pesan_saat_ini)


daftar_pesan = [
    "Hai, udah makan belum?",
        "Kalo belum ayo ke warjaw",
        "Makasih ya kemarin udah bantu!",
]
pesan_terkirim = []

# Kirim salinan daftar, supaya daftar aslinya tetap utuh.
kirim_pesan(daftar_pesan[:], pesan_terkirim)

print(f"\nDaftar pesan (asli): {daftar_pesan}")
print(f"Pesan terkirim: {pesan_terkirim}")