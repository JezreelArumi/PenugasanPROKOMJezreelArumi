# 8.13 User Profile (Profil Pengguna)
def buat_profil(nama_depan, nama_belakang, **info_pengguna):
    """Buat dictionary berisi semua yang kita ketahui tentang pengguna."""
    info_pengguna['nama_depan'] = nama_depan
    info_pengguna['nama_belakang'] = nama_belakang
    return info_pengguna


profil_saya = buat_profil('Jezreel', 'Arumi',
                          kota='Denpasar',
                          hobi='bermain gitar',
                          pekerjaan='mahasiswa')
print(profil_saya)