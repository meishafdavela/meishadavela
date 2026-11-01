guest=['salsa', 'neejad', 'nayya', 'sherin', 'zahrah', 'fania', 'kayla']

print("I'm sorry, but I can only invite two people to dinner.")
while len(guest) > 2:
    removed_guest = guest.pop()
    print(f"I'm sorry, {removed_guest}, I can't invite you to dinner.")

print(f"{guest[0]}, you are still invited to dinner.")
print(f"{guest[1]}, you are still invited to dinner.")

del guest[0]
del guest[0]

print(guest)