from pathlib import Path
 
 
def count_the(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        lowered = contents.lower()
        count_plain = lowered.count('the')
        count_space = lowered.count('the ')
        print(f"\n{path}")
        print(f"  'the' appears about {count_plain} times.")
        print(f"  'the ' (with a space) appears about {count_space} times.")
 
 
filenames = ['alice.txt', 'moby_dick.txt']
for filename in filenames:
    path = Path(filename)
    count_the(path)