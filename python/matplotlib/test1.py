import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

plt.rcParams['font.size'] = 18
plt.rcParams["figure.figsize"] = (20,15)

fig, ax = plt.subplots()
ax.grid()

param_a = np.arange(0, 5, 0.2)
x = np.arange(-10, 10, 0.1)
y = x*x
plot1, = plt.plot(x, y)

ind = 5
ax.set_title(f"y = {param_a[ind]:.2f}*x*x")

def click_next(event):
    global ind
    ind += 1
    i = ind % len(param_a)
    ydata = param_a[i]*x*x
    plot1.set_ydata(ydata)
    ax.set_title(f"y = {param_a[i]:.2f}*x*x")
    plt.draw()

def click_prev(event):
    global ind
    ind -= 1
    i = ind % len(param_a)
    ydata = param_a[i]*x*x
    ax.set_title(f"y = {param_a[i]:.2f}*x*x")
    plot1.set_ydata(ydata)
    plt.draw()

axprev = plt.axes([0.6, 0.02, 0.05, 0.05])
axnext = plt.axes([0.7, 0.02, 0.05, 0.05])
bnext = Button(axnext, 'Next')
bnext.on_clicked(click_next)
bprev = Button(axprev, 'Prev')
bprev.on_clicked(click_prev)

plt.show()
