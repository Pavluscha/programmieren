String = input("Bei welchem Wort/Satz sollen die Buchstaben gezahlt werden? :")
chars = list(String)

dict = {}

for char in chars:
    if char in dict:
        dict[char] += 1
    else:
        dict.update({char: 1})

print(dict)