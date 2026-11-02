# 8.17 Styling Functions (b) (Gaya Fungsi): kota, dari Latihan 8.5
# Dicek: docstring ada, nilai bawaan ditulis negara='Indonesia' tanpa
# spasi, dan baris kode tidak lebih dari 79 karakter.
def deskripsikan_kota(nama_kota, negara='Indonesia'):
    """Tampilkan kalimat sederhana tentang lokasi sebuah kota."""
    print(f"{nama_kota.title()} ada di {negara.title()}.")


deskripsikan_kota('surakarta')
deskripsikan_kota('bandung')
deskripsikan_kota('reykjavik', negara='islandia')