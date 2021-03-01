import numpy as np
import matplotlib.pyplot as plt


#
#
# def cos(x):
#     return np.sin(x)
# def plot_function(f, x_min=-10, x_max=10, n_values=2000):
#     x = np.linspace(x_min, x_max, n_values)
#     y = f(x)
#     plt.plot(x, y)
#     plt.show()
#
#
# # plot_function(lambda x: np.sin(x))
# plot_function(lambda x: cos(x))
#
# def plot_function(f, x_min=-10, x_max=10, n_values=4):
#     plt.gca().set_aspect("equal")
#     x = np.linspace(x_min, x_max, n_values)
#     y = f(x)
#     plt.plot(x, y)
#
#
# plot_function(lambda x: np.sqrt(1 - x ** 2), -1, 1)
# plot_function(lambda x: -np.sqrt(1 - x ** 2), -1, 1)
# plt.show()


r = 1 # Radius
phi = np.linspace(0, 2 * np.pi, 1000) # Angle (full circle)
# x = r * np.cos(phi)
# y = r * np.sin(phi)
# plt.plot(x, y)

plt.polar(phi, r)
plt.gca().set_aspect("equal")
plt.show()

plt.polar(phi, r)


