# 6.5 Rivers
sungai = {
    'nil': 'mesir',
    'amazon': 'brazil',
    'yangtze': 'china',
}

for sungai_name, negara in sungai.items():
    print(f"The {sungai_name.title()} runs through {negara.title()}.")

print("\nThe rivers included in the dictionary are:")
for sungai_name in sungai.keys():
    print(sungai_name.title())

print("\nThe countries included in the dictionary are:")
for negara in sungai.values():
    print(negara.title())