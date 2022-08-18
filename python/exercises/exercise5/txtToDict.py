f = open("data.txt","r")
Lines = f.readlines()

txtToDict = {}


for line in Lines:
    str = line.strip()
    keys_values = str.split(":")
    #print(keys_values)
    txtToDict.update({keys_values[0]: keys_values[1]})
    
print(txtToDict)
