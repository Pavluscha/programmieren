string = "hallo ich mochte ein haus haben"
first_char = string[0]


for char in string:
    if char == first_char:
        string = string.replace(char, "$")

string = first_char + string[1:]
print(string)
