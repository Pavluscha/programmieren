import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

plt.rcParams['font.size'] = 18
plt.rcParams["figure.figsize"] = (16,8)

fig, ax = plt.subplots()
ax.grid()

ind_y = 0
ind_x = 0

xpoints = np.arange(-5, 5, 0.1)
ypoints = xpoints * xpoints
plot1, = ax.plot(xpoints, ypoints)

def draw_plot():
    ypoints = (xpoints - ind_x) * (xpoints - ind_x) + ind_y
    plot1.set_ydata(ypoints)
    plt.draw()
    

def click_top(event):
    global ind_y
    ind_y += 1
    draw_plot()

def click_down(event):
    global ind_y
    ind_y -= 1
    draw_plot()

def click_left(event):
    global ind_x
    ind_x -= 1
    draw_plot()

def click_right(event):
    global ind_x
    ind_x += 1
    draw_plot()

axtop = plt.axes([0.1, 0.89, 0.03, 0.04])
btop = Button(axtop, 'Top')
btop.on_clicked(click_top)

axdown = plt.axes([0.2, 0.89, 0.03, 0.04])
bdown = Button(axdown, 'Down')
bdown.on_clicked(click_down)

axleft = plt.axes([0.3, 0.89, 0.03, 0.04])
bleft = Button(axleft, 'Left')
bleft.on_clicked(click_left)

axright = plt.axes([0.4, 0.89, 0.03, 0.04])
bright = Button(axright, 'Right')
bright.on_clicked(click_right)

draw_plot()
plt.show()

