import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv



header=("step","vid","acc","speed","pos","lane")

# load data from csv file
data = pd.read_csv("../data/data.csv",names=header)


# extract the relevant columns
steps = np.array(data["step"])
positions = np.array(data["pos"])
speeds = np.array(data["speed"])

# create a 2D array with x=step, y=pos, z=speed
heatmap, xedges, yedges = np.histogram2d(steps, positions, weights=speeds, bins=(100,40))
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

# plot the heatmap using imshow
plt.imshow(heatmap.T, origin='lower',interpolation="bicubic",)
plt.xlabel("Step")
plt.ylabel("Pos")
plt.colorbar()
plt.show()

