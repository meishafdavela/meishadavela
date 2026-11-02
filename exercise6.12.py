person = {
    'first_name': 'Meisha',
    'last_name': 'Davela',
    'age': 18,
    'city': 'New York',
}
person_2={
    'first_name': 'Salsabila',
    'last_name': 'Berliana',
    'age': 18,
    'city': 'Yogyakarta',
}
person_3={
    'first_name': 'Nayyara',
    'last_name': 'Najma',
    'age': 18,
    'city': 'Jakarta',
}
people = [person, person_2, person_3]
people[0]['hobby'] = 'reading'
people[1]['hobby'] = 'cooking'
people[2]['hobby'] = 'football' 
for person_info in people:
    full_name = f"{person_info['first_name']} {person_info['last_name']}"
    print(full_name)
    print(f"\tAge: {person_info['age']}")
    print(f"\tCity: {person_info['city']}")
    print(f"\tHobby: {person_info['hobby']}\n")