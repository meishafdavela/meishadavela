# pi_birthday.py
from pathlib import Path

path = Path(__file__).parent / 'pi_million_digits.txt'
contents = path.read_text(encoding='utf-8')
pi_string = ''
for line in contents.splitlines():
    pi_string += line.lstrip()
    
print("\npi_string:")
print(pi_string)