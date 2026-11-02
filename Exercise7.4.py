# 7.4 Pizza Toppings (Topping Pizza)
pesan_prompt = "\nTopping apa yang Anda inginkan di pizza Anda?"
pesan_prompt += "\nKetik 'keluar' jika sudah selesai. "

topping = ""
while topping != 'keluar':
    topping = input(pesan_prompt)

    if topping != 'keluar':
        print(f"Saya tambahkan {topping} ke pizza Anda.")