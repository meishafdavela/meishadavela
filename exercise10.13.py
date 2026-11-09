from pathlib import Path
import json
 
path = Path('user_info.json')
 
if path.exists():
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f"Welcome back, {user_info['name']}!")
else:
    user_info = {}
    user_info['name'] = input("What is your name? ")
    user_info['city'] = input("Which city do you live in? ")
    user_info['hobby'] = input("What is your favorite hobby? ")
 
    contents = json.dumps(user_info)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {user_info['name']}!")
 
print("\nHere is what I remember about you:")
print(f"Name: {user_info['name']}")
print(f"City: {user_info['city']}")
print(f"Hobby: {user_info['hobby']}")