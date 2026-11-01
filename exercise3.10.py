languages = ['English', 'Javanese', 'Japanese', 'Indonesia',]

languages.append('Chinese')
languages.insert(1, 'Korean')
print("3-10 sebelum ubah:", languages)

languages[0] = 'Spanish'
print("setelah ubah:", languages)

languages.remove('Chinese')
last = languages.pop()
print(f"pop() membuang: {last}")

del languages[1] 
print("sisa:", languages)
print("sorted():", sorted(languages))

languages.sort() 
print("sort():", languages)

languages.reverse()
print("reverse():", languages)

print("len():", len(languages))