# 8.9 Messages (Daftar Pesan)
def tampilkan_pesan(daftar_pesan):
    """Cetak setiap pesan teks dalam daftar."""
    for pesan in daftar_pesan:
        print(pesan)


daftar_pesan = [
    "Hai, udah makan belum?",
    "Kalo belum ayo ke warjaw",
    "Makasih ya kemarin udah bantu!",
]
tampilkan_pesan(daftar_pesan)