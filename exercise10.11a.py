# save_favorite_number.py

from pathlib import Path
import json
 
number = int(input("What is your favorite number? "))
 
path = Path('favorite_number.json')
contents = json.dumps(number)
path.write_text(contents)
 
print("Thanks, I've saved your favorite number.")