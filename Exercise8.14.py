# 8.14 Cars (Mobil)
def buat_mobil(pabrikan, model, **fitur_tambahan):
    """Simpan informasi sebuah mobil dalam dictionary."""
    mobil = {'pabrikan': pabrikan, 'model': model}
    for nama_fitur, nilai in fitur_tambahan.items():
        mobil[nama_fitur] = nilai
    return mobil


mobil = buat_mobil('subaru', 'outback', warna='biru', paket_derek=True)
print(mobil)