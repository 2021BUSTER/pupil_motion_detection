import matplotlib.pyplot as plt
import seaborn as sns

cm = [
    [0, 100, 106, 0],
    [200, 704, 821, 215],
    [128, 689, 758, 130],
    [0, 331, 368, 128]
]

ax = sns.heatmap(cm, cmap='Blues', cbar=False , vmin = 0, vmax = 1000)
ax.tick_params(left=False, bottom=False)
ax.axes.xaxis.set_visible(False)
ax.axes.yaxis.set_visible(False)
     
plt.savefig('savefig_200dpi.png', dpi=200)
