# 8.7 Album
def buat_album(artis, judul, jumlah_lagu=None):
    """Kembalikan dictionary berisi informasi sebuah album."""
    album = {'artis': artis, 'judul': judul}
    if jumlah_lagu:
        album['jumlah_lagu'] = jumlah_lagu
    return album


album_1 = buat_album('reality club', 'reality club presents...')
print(album_1)

album_2 = buat_album('hindia', 'menari dengan bayangan')
print(album_2)

album_3 = buat_album('nadin amizah', 'untuk dunia, cinta, dan kotornya')
print(album_3)

# Pemanggilan yang menyertakan jumlah lagu.
album_4 = buat_album('cortis', 'greengreen', jumlah_lagu=9)
print(album_4)