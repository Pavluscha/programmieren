import json
from pickle import TRUE
from pprint import pprint

f = open('gesamt_dict.json')
data = json.load(f)
f.close()

for land in data:
    bevolkerung = data[land]["bevolkerung"]
    bip = data[land]["bip"]
    bipProKopf = (bip / bevolkerung) * 1000000
    data[land]["bipProKopf"] = bipProKopf

def printTable():
    formatTableHead = "{:<15}{:<20}{:<15}{:<15}{:<15}{:<15}" 
    formatTable = "{:<15}{:<20,}{:<15,}{:<15,}{:<15}{:<15.2f}"  
    print(formatTableHead.format('Länder','Bevölkerung','BIP','Fläche', 'Währung', 'BipProKopf'))
    for land in sorted(data):
        print(formatTable.format(land, data[land]["bevolkerung"], data[land]["bip"], data[land]["territorie"], data[land]["wahrung"] , data[land]["bipProKopf"]))   

def printSortedTable(sortIndex):
    formatTableHead = "{:<15}{:<20}{:<15}{:<15}{:<15}{:<15}" 
    formatTable = "{:<15}{:<20,}{:<15,}{:<15,}{:<15}{:<15.2f}"  
    print(formatTableHead.format('Länder','Bevölkerung','BIP','Fläche', 'Währung', 'BipProKopf'))
    for land in sortIndex:
        print(formatTable.format(land, data[land]["bevolkerung"], data[land]["bip"], data[land]["territorie"], data[land]["wahrung"], data[land]["bipProKopf"] ))

indexBipProKopf = sorted(data , key= lambda x: data[x]["bipProKopf"], reverse=True)


printSortedTable(indexBipProKopf)
#pprint(data)




