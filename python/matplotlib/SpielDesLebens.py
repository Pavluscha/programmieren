import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import time
from array import *

plt.rcParams["figure.figsize"] = (7,7)

Feld = []

for i in range(0, 21):
    zeile = []
    for i in range(0,21):
        zeile.append(0)
    Feld.append(zeile)


        


game_state = "beginnig"

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

schritte = np.arange(0.5, 21.5, 1)

ax.set_xticks(schritte)
ax.set_yticks(schritte)

ax.grid(which='major', alpha=1)

def onclick(event):
    xpoint = round(event.xdata)
    ypoint = round(event.ydata)
    if game_state == "beginnig":
        if Feld[xpoint][ypoint] == 1:
            pass
        else:
            Feld[xpoint][ypoint] = 1
            punkt_spawn(xpoint, ypoint)
            find_neighbours(xpoint,ypoint)


def punkt_spawn(x, y):
    plt.scatter(x, y, s= 200, c= "blue")
    plt.draw()
    

def find_neighbours(xpoint,ypoint):

    neighbours = []

    for i in range(0, 21):
        zeile = []
        for i in range(0,21):
            zeile.append(0)
        neighbours.append(zeile)
    
    neighbours[xpoint + 1][ypoint] = 1
    neighbours[xpoint - 1][ypoint] = 1
    neighbours[xpoint][ypoint + 1] = 1
    neighbours[xpoint][ypoint - 1] = 1
    neighbours[xpoint - 1][ypoint - 1] = 1
    neighbours[xpoint + 1][ypoint - 1] = 1
    neighbours[xpoint - 1][ypoint + 1] = 1
    neighbours[xpoint + 1][ypoint + 1] = 1

    for x in range(1, 21):
        for y in range(1,21):
            if neighbours[x][y] == 1:
               plt.scatter(x,y, s= 100, c= "green")

    plt.draw()


fig.canvas.mpl_connect('button_press_event', onclick)

plt.xlim([0.5, 20.5])
plt.ylim([0.5, 20.5])
plt.show()