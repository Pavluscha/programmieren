d = {'Name': 'David', 'Email': 'david@gmail.com', 'Phone': '33354587', 'Age': '27'}

f= open("data.txt","w+")

for x, y  in d.items():
    f.write(x + ": " + y + "\n")