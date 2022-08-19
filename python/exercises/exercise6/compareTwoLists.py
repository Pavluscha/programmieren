listOfSameValues = []

def compareFunction(firstList, secondList):
    for char in firstList:
        for secondChar in secondList:
            if char == secondChar:
                listOfSameValues.append(char)

compareFunction(["apple", "banana", "cherry", "mangoes", "oranges"], ["ananas", "apple", "kiwi", "oranges", "peach"])

print(listOfSameValues)