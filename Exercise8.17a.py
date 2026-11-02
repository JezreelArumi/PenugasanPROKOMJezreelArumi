# 8.17 Styling Functions (a) (Gaya Fungsi): kaos, dari Latihan 8.4
# Dicek: nama huruf kecil dengan underscore, docstring tepat setelah def,
# tanpa spasi di sekitar tanda = pada nilai bawaan dan argumen kata kunci,
# serta dua baris kosong setelah definisi fungsi.
def buat_kaos(ukuran='besar', tulisan='Saya cinta Python'):
    """Tampilkan ringkasan kaos. Bawaannya ukuran besar."""
    print(f"\nKaos ukuran {ukuran} dengan tulisan '{tulisan}'.")


buat_kaos()
buat_kaos('sedang')
buat_kaos(ukuran='kecil', tulisan='Kode itu seni')