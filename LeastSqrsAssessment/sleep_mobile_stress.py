import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D

ax = plt.axes(projection='3d')

file = "sleep_mobile_stress_dataset_15000.csv"

def get_data(file):
    with open(file) as f:
        reader = csv.reader(f)
        next(reader)
        data = list(reader)
    return data

d = get_data(file)

filtered_data = []
xdata = []          # daily phone usage (hours)
ydata = []          # sleep duration (hours)
zdata= []           # stress level (scale from 1-10)
for row in d:
    sub = [float(row[4]), float(row[6]), float(row[8])]
    xdata.append(float(row[4]))
    ydata.append(float(row[6]))
    zdata.append(float(row[8]))
    filtered_data.append(sub)

# for i in range(6):
#     sub = [float(d[i][4]), float(d[i][6]), float(d[i][8])]
#     xdata.append(float(d[i][4]))
#     ydata.append(float(d[i][6]))
#     zdata.append(float(d[i][8]))
#     filtered_data.append(sub)

arr1 = np.ones(len(filtered_data))

newarr = np.concatenate((xdata, ydata, arr1))
M = np.reshape(newarr, (3,len(filtered_data)))
result = np.linalg.inv((M @ M.T)) @ M @ zdata
print(result)
slopex = result[0]
slopey = result[1]
intercept = result[2]
x,y= np.meshgrid(range(0, 10, 1), range(0, 10, 1))
z = x * slopex + y * slopey + intercept

# Here we define the set of x- and y-coordinates beforehand
# The 'ro' option yields red unconnected dots
#plt.plot(xdata,ydata, 'ro')

ax.plot_surface(x, y, z, alpha = 0.4)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)

# Create the 3D plot
ax.scatter3D(xdata,ydata,zdata, c=zdata, cmap='inferno_r', vmin=0.2)
ax.set_xlabel("phone usage")
ax.set_ylabel("sleep duration")
ax.set_zlabel("stress level")

ax.text(-5, 10, 12, rf'$z = {round(slopex, 2)}x + {round(slopey, 2)}y + {round(intercept, 2)}$', fontsize=14)

# Display the plot object
# Commented out because it does not work in GitHub Codespaces
#plt.show()

# Save the plot object as a png
plt.savefig('Sleep_Data_output.png')