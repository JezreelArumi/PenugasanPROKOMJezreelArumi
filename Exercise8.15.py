"""Modul berisi fungsi-fungsi untuk mencetak model 3D."""


def cetak_model(desain_belum_dicetak, model_selesai):
    """
    Simulasikan pencetakan setiap desain sampai habis.
    Pindahkan setiap desain ke model_selesai setelah dicetak.
    """
    while desain_belum_dicetak:
        desain_saat_ini = desain_belum_dicetak.pop()
        print(f"Mencetak model: {desain_saat_ini}")
        model_selesai.append(desain_saat_ini)


def tampilkan_model_selesai(model_selesai):
    """Tampilkan semua model yang sudah dicetak."""
    print("\nModel berikut sudah dicetak:")
    for model in model_selesai:
        print(model)