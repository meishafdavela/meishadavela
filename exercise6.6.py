favorite_languages = {
    'Vela': 'Russian',
    'Nayya': 'Chinese',
    'Salsa': 'French',
    'Maria': 'English',
}
people_to_poll = ['Vela', 'Nayya', 'Salsa', 'Maria', 'Zahrah']

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"{name.title()}, please take our favorite languages poll!")