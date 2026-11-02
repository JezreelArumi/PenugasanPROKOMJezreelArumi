# 8.3 T-Shirt (Kaos)
def buat_kaos(ukuran, tulisan):
    """Tampilkan ringkasan ukuran kaos dan tulisan di atasnya."""
    print(f"\nKaos ukuran {ukuran} dengan tulisan '{tulisan}'.")


# Pemanggilan pertama: argumen posisi.
buat_kaos('M', 'Is it better to speak or to die?')

# Pemanggilan kedua: argumen kata kunci.
buat_kaos(tulisan='Is it better to speak or to die?', ukuran='L')