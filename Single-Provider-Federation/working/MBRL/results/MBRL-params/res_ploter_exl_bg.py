import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

font = {
            'weight' : 'bold',
            'size'   : 15
        }

matplotlib.rc('font', **font)
matplotlib.rcParams["axes.labelweight"] = "bold"
matplotlib.rcParams["axes.labelsize"] = "18"

# Make data.
X_range = np.arange(0, 6, 1)
Y_range = np.array([0, 5, 10, 20])

X, Y = np.meshgrid(X_range, Y_range)
print("X = ", X)
print("Y = ", Y)

Z = np.array([
      	[29.21332701, 29.22453959, 29.69284886, 30.06122754, 30.01365946, 30.21365946], 
	[30.01165248, 29.97085549, 38.49761008, 43.6857773, 44.84380451, 46.2906724],
	[29.89406598, 29.60695341, 43.93459973, 48.01979302, 50.28779241, 50.28110436],
	[29.65561494, 29.46848386, 45.24444008, 49.1292123, 51.13574245, 51.42534383]
    ])

print("Z = ", Z)

ax.view_init(15, -135)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.set_xlim(0.00, 5.00)
#plt.xlabel(r'$\kappa$')
ax.set_xlabel(r'$\kappa$')
ax.xaxis.set_major_locator(LinearLocator(6))

ax.set_ylim(0.00, 20.00)
#plt.ylabel(r'$\theta$')
ax.set_ylabel(r'$\theta$')
ax.yaxis.set_major_locator(LinearLocator(5))

ax.set_zlim(29, 55)
ax.zaxis.set_rotate_label(False)
ax.set_zlabel("Average Profit", fontweight = 'bold', fontsize=12, rotation=90)
ax.zaxis.set_major_locator(LinearLocator(5))


plt.savefig("param_exl_bg.pdf",  bbox_inches='tight', pad_inches=0.15, format="pdf",transparent=True)

