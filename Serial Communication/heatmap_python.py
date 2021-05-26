import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

cm = [
    [0, 100, 106],
    [200, 704, 821],
    [128, 689, 758]
]

j = 0
data = list(range(0,16))
for i in range(0,16) :
    if i % 4 == 0 or i > 11:
        data[i] = 0
    else :
        data[i] = int(cm[j])
        j = j+1

ax = sns.heatmap(data, cmap='Greys', cbar=False , vmin = 0, vmax = 1024)
ax.tick_params(left=False, bottom=False)
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)

     
plt.savefig('savefig_200dpi.png', dpi=200)
