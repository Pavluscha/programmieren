import json
from timeit import timeit
from array import array
import re
import sys

lander = ["RUS", "GER", "USA", "CHN", "JPN", "GBR", "IND", "ITA", "BRA", "TUR"]

bevolkerung = [145872260, 83517046, 329064917, 1433783692, 126860299, 67530172, 1366417756, 60100075, 211049519, 83429607]
bip = [1478570, 3843340, 20893750, 14866740, 5045100, 2709680, 2660240, 1884940, 1444720, 719919] #in Millionen
territorie = [17098242, 357022, 9525067, 9596960, 377975, 243610, 3287263, 301340, 8515770, 783562] #in km^2
wahrung = ["Rubel", "Euro", "Dollar", "Renminbi", "Yen", "Pfund", "Rupie", "Euro", "Real", "Lira"]

data = {}

for i in range(0, len(lander)):
    land = lander[i]
    data[land] = {
        "bevolkerung": bevolkerung[i],
        "bip": bip[i],
        "territorie": territorie[i],
        "wahrung": wahrung[i]
    }
    

out_file = open("gesamt_dict.json", "w")
json.dump(data, out_file, indent = 2)
out_file.close()

arrayBipProKopf = []



for i in range (0, len(lander)):
    arrayBipProKopf.append(bip[i] * 1000000 / bevolkerung[i])



def sortBipProKopf():
    CopyBipProKopf = []
    for i in range (0, len(lander)):
        CopyBipProKopf.append(arrayBipProKopf[i])
    def sucheBiggest():
        biggest = 0
        biggestIndex = 0
        for i in range (0, len(lander)):
            if CopyBipProKopf[i] > biggest:
                biggest = CopyBipProKopf[i]
                biggestIndex = i
        
        return biggestIndex

    Reihenfolge = []
    for i in range (0, len(lander)):
        k = sucheBiggest()
        Reihenfolge.append(k)
        CopyBipProKopf[k] = 0

    return Reihenfolge


def printAll01():
    for i in range (0, len(lander)):
        print(lander[i] + ":")
        print(f" bevölkerung: {bevolkerung[i]:,}")
        print(f" Bruttoinlandsprodukt: {bip[i]:,} $")
        print(f" Fläche: {territorie[i]:,} km^2")
        print(" Währung: " + str(wahrung[i]) + "\n")

def printTable():
    formatTableHead = "{:<15}{:<20}{:<15}{:<15}{:<15}" 
    formatTable = "{:<15}{:<20,}{:<15,}{:<15,}{:<15}"  
    print(formatTableHead.format('Länder','Bevölkerung','BIP','Fläche', 'Währung'))
    for i in range (0, len(lander)):
        print(formatTable.format(lander[i], bevolkerung[i], bip[i], territorie[i], wahrung[i]))   

def landInfo(land):
    i = findIndex(land) 
    print(lander[i] + ":")
    print(f" bevölkerung: {bevolkerung[i]:,}")
    print(f" Bruttoinlandsprodukt: {bip[i]:,} $")
    print(f" Fläche: {territorie[i]:,} km^2")
    print(" Währung: " + str(wahrung[i]) + "\n")



def findIndex(land):
    for i in range (0, len(lander)):
        if lander[i] == land:
            return i
    raise Exception(f"Error: land {land} not found")


def printVergleich():
    for i in range (0, len(lander)):
        print(lander[i] + ":")
        print(f" {arrayBipProKopf[i]:.2f}")


#landInfo("BRA")
#printTable()
#printVergleich()
def test1():
    index = sortBipProKopf()
def test2():
    index = sorted(range(0,10) , key= lambda x: arrayBipProKopf[x], reverse=True)

result = timeit(test1, number=1000000)
print("Time in seconds test1:", result)

result = timeit(test2, number=1000000)
print("Time in seconds test2:", result)

def printSortedTable(sortedIndex):
    formatTableHead = "{:<15}{:<20}{:<15}{:<15}{:<15}{:<15}" 
    formatTable = "{:<15}{:<20,}{:<15,}{:<15,}{:<15}{:<15.2f}"  
    print(formatTableHead.format('Länder','Bevölkerung','BIP','Fläche', 'Währung', 'BIP-Kopf'))
    for i in sortedIndex:
        print(formatTable.format(lander[i], bevolkerung[i], bip[i], territorie[i], wahrung[i], arrayBipProKopf[i]))   

#printSortedTable(index)


