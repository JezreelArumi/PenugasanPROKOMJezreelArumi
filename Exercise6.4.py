# 6.4 Glossary 2
glossary = {
    'string': 'karakter dalam kutipan.',
    'list': 'item dengan urutan tertentu.',
    'variable': 'nama yang mewakili sebuah nilai.',
    'comment': 'catatan dalam pemrograman yang diabaikan Python.',
    'tuple': 'daftar item yang tidak bisa diganti.',
    # Five more terms. The loop below prints them automatically.
    'float': 'angka desimal.',
    'method': 'tindakan yang dapat dilakukan Python pada sepotong data.',
    'index': 'posisi dari sebuah item dalam sebuah list, dimulai dari 0.',
    'loop': 'kode yang diulang sekali untuk setiap item atau selama sebuah ujian adalah True.',
    'dictionary': 'kumpulan pasangan kunci-nilai.',
}

for word, meaning in glossary.items():
    print(f"{word}:\n\t{meaning}\n")