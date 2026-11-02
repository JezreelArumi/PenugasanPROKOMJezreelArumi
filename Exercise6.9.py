# 6.9 Favorite Places
favorite_places = {
    'maria': ['lisbon', 'kyoto'],
    'chen': ['banff national park', 'singapore', 'santorini'],
    'sofia': ['buenos aires'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")