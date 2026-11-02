favorite_numbers = {
    'nayya': [7,17],
    'neejad': [3,33],
    'vela': [13, 31],
    'salsa': [5],
    'kayla': [0, 14, 9],
}
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")