favorite_places = {
    'Vela': ['surabaya', 'bandung'],
    'Salsa': ['yogyakarta'],
    'Nayya': ['bali', 'raja ampat', 'malang'],
}
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")