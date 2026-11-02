# 8.12 Sandwiches (Sandwich)
def pesan_sandwich(*bahan):
    """Tampilkan ringkasan sandwich yang sedang dipesan."""
    print("\nMembuat sandwich dengan bahan berikut:")
    for bahan_tambahan in bahan:
        print(f"- {bahan_tambahan}")


pesan_sandwich('ham')
pesan_sandwich('tuna', 'selada', 'tomat')
pesan_sandwich('ayam', 'keju', 'timun', 'saus sambal', 'mayones')