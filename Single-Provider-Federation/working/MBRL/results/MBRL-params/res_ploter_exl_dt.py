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
Y_range = np.arange(0, 6, 1)

X, Y = np.meshgrid(X_range, Y_range)
print("X = ", X)
print("Y = ", Y)

Z = np.array([
      	[30.04719267, 29.90602266, 30.04970276, 29.54796269, 29.62051109, 29.97299639],
	[29.87597864, 44.31455497, 48.58210817, 49.28303607, 50.20333581, 49.90993671],
	[29.55858868, 51.09402421, 51.1541318, 51.56266505, 51.95029401, 52.07015197], 
	[29.60116421, 51.74652668, 51.31689163, 52.71937626, 50.73691093, 49.32308723],
	[29.69798548, 54.18226538, 51.40840282, 50.72933928, 50.15286899, 48.58542404],
	[29.69289435, 54.04258078, 55.00865312, 52.34574104, 48.66509369, 49.0572977]
    ])

print("Z = ", Z)

ax.view_init(35, -120)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.set_xlim(0.00, 5.00)
ax.set_xlabel(r'$\kappa$')
ax.xaxis.set_major_locator(LinearLocator(6))

ax.set_ylim(0.00, 5.00)
ax.set_ylabel(r'$\theta$')
ax.yaxis.set_major_locator(LinearLocator(6))

ax.set_zlim(29, 55)
ax.zaxis.set_rotate_label(False)
ax.set_zlabel("Average Profit", fontweight = 'bold', fontsize=12, rotation=90)
ax.zaxis.set_major_locator(LinearLocator(5))

plt.savefig("param_exl_dt.pdf", bbox_inches='tight', pad_inches=0.15, format="pdf",transparent=True)

