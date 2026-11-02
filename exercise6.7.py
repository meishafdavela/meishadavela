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
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    
    print(f"Name: {full_name}")
    print(f"Age: {age}")
    print(f"City: {city}\n")