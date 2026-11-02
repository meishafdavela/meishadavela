pet_1 = {'kind': 'cat', 'owner': 'budi'}
pet_2 = {'kind': 'dog', 'owner': 'siti'}
pet_3 = {'kind': 'rabbit', 'owner': 'andi'}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(f"Kind of animal: {pet['kind']}")
    print(f"Owner: {pet['owner'].title()}\n")