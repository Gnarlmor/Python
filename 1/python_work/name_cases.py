name = "Eric"
message = f"Hello {name}, would you like to learn some Python today?"
print(message)

name_1 = "linda"
print(name_1.lower())
print(name_1.upper())
print(name_1.title())

name_2 = "Mahmoud"
surname_2 = "Darwish"
message = f'{name_2} {surname_2} once said, "I have enough memories to drink coffee all by myself in a cafe, so empty yet so crowded with the gosts of those who have left but always stayed."'
print(message)

name_3 = '  \t\nGrigore  '
print(name_3)
print(name_3.lstrip())
print(name_3.rstrip())
print(name_3.strip())

filename = 'python_notes.txt'
filename = filename.removesuffix('.txt')
print(filename)