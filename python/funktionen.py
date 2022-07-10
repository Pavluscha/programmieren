import matplotlib.pyplot as plt
import numpy as np
from random import seed
from random import randint
from random import random
import math 

anfangs_x = 100
anfangs_y = 0

punktposx = randint(1, 31)
punktposy = randint(1, 31)
print("punkt:")

def punkt_und_flache(x):
    m = punktposy / (x - punktposx)
    punkt_links_y = (x * m)
    current_flache = (x * punkt_links_y) / 2
    return punkt_links_y, current_flache

def abstand(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    c = math.sqrt(x*x + y*y)
    return c

current_x = anfangs_x
current_y = anfangs_y
current_punkt_links, current_flache = punkt_und_flache(current_x)

while True:
    new_x = current_x - 0.1
    new_punkt_links, new_flache = punkt_und_flache(new_x)
    if new_flache < current_flache:
        current_x = new_x
        current_flache = new_flache
        current_punkt_links = new_punkt_links
    else:
        break

abstand_1 = abstand( (current_x, 0), (punktposx, punktposy) )
abstand_2 = abstand( (0, current_punkt_links), (punktposx, punktposy) )

print(abstand_1, abstand_2)

#print(current_flache)
xpoints = [0,current_x]
ypoints = [current_punkt_links,current_y]

plt.plot(xpoints, ypoints)
plt.plot([punktposx], [punktposy], 'o')
plt.xlim([0, 50])
plt.ylim([0, 50])
plt.show()