# 8.6 City Names (Nama Kota)
def kota_negara(kota, negara):
    """Kembalikan kota dan negara dalam format 'Kota, Negara'."""
    hasil = f"{kota}, {negara}"
    return hasil.title()


paris = kota_negara('paris', 'prancis')
print(paris)

tokyo = kota_negara('tokyo', 'jepang')
print(tokyo)

sydney = kota_negara('sydney', 'australia')
print(sydney)