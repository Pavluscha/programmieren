import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

plt.rcParams['font.size'] = 18
plt.rcParams["figure.figsize"] = (40,12)

fig, ax = plt.subplots()
ax.grid()

param_a = np.arange(0, 5, 0.2)
x = np.arange(-10, 10, 0.1)

ind = 5
i = ind % len(param_a)
ydata = param_a[i]*x*x
plot1, = ax.plot(x,ydata)
ax.set_title(f"y = {param_a[ind]:.2f}*x*x")

def draw_plot():
    i = ind % len(param_a)
    ydata = param_a[i]*x*x
    plot1.set_ydata(ydata)
    ax.set_title(f"y = {param_a[i]:.2f}*x*x")
    plt.draw()

def click_next(event):
    global ind
    ind += 1
    draw_plot()

def click_prev(event):
    global ind
    ind -= 1
    draw_plot()

axprev = plt.axes([0.1, 0.89, 0.03, 0.04])
axnext = plt.axes([0.14, 0.89, 0.03, 0.04])
bnext = Button(axnext, 'Next')
bnext.on_clicked(click_next)
bprev = Button(axprev, 'Prev')
bprev.on_clicked(click_prev)

draw_plot()
plt.show()
