places=['Tokyo', 'Los Angeles', 'Swiss', 'Penang', 'Guangzhou']
print('Original List:', places)

print('sorted:', sorted(places))
print('after sorted', places)

print("Original list again:", places)

print('reversed:', sorted(places, reverse=True))
print('setelah reversed', places)

print("Original list again:", places)

places.reverse()
print('reversed list:', places)

places.reverse()
print('Original list again:', places)

places.sort()
print('Alphabetical order list:', places)

places.sort(reverse=True)
print('Reverse Alphabetical order list:',places)