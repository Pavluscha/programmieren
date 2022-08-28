import matplotlib
from matplotlib import pyplot as plt, patches

#plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
fig.set_dpi(200)
fig.set_size_inches(7, 7)
ax = fig.add_subplot(111)
rect = patches.Rectangle((2, 2), 8, 5, color='yellow')
circle = patches.Circle((6, 4.5), radius=2, color='red')
ax.add_patch(rect)
ax.add_patch(circle)
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.axis('equal')
plt.grid()
plt.show()
