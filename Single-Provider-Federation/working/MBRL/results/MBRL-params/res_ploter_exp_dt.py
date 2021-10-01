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
  	[30.22003911, 29.8392302, 29.60071837, 29.69781351, 30.00736399, 29.60071837], 
   	[29.94892046, 43.05712552, 47.59180361, 46.40458407, 47.60624596, 46.91781688],
   	[30.13691087, 42.61825057, 47.36615964, 46.60370656, 48.02978559, 47.46451623], 
   	[29.6778791, 43.3168408, 46.73996624, 47.77692394, 47.50808843, 49.04289686],
   	[30.08498338, 44.75949261, 46.55643339, 47.90367577, 49.84843711, 49.79116944], 
   	[30.0304684, 42.15257548, 47.32457908, 48.74630915, 49.5657802, 48.80218017]   
       ])

print("Z = ", Z)

ax.view_init(20, -120)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.set_xlim(0.00, 5.00)
ax.set_xlabel(r'$\kappa$', fontsize=15)
ax.xaxis.set_major_locator(LinearLocator(6))

ax.set_ylim(0.00, 5.00)
ax.set_ylabel(r'$\theta$', fontsize=15)
ax.yaxis.set_major_locator(LinearLocator(6))

ax.set_zlim(29, 55)
ax.zaxis.set_rotate_label(False)
ax.set_zlabel("Average Profit", fontweight = 'bold', fontsize=15, rotation=90)
ax.zaxis.set_major_locator(LinearLocator(5))

ax.tick_params(labelsize=12)


plt.savefig("param_exp_dt.pdf", bbox_inches='tight', pad_inches=0.1, format="pdf",transparent=True)

