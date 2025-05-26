import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# === 1. Carrega dados do FreeFEM ===
# Assuma que você salvou os perfis previamente com esse nome
# u ao longo de y no centro vertical (x = 0.5)
freefem_y, freefem_u1 = np.loadtxt("perfil_u1_x05_Re1000.txt", unpack=True)
# v ao longo de x no centro horizontal (y = 0.5)
freefem_x, freefem_u2 = np.loadtxt("perfil_u2_y05_Re1000.txt", unpack=True)

# === 2. Dados brutos de Ghia et al. (1982) ===

# # u(x=0.5, y) Re = 100
# ghia_y_u1 = np.array([1.0000, 0.9766, 0.9688, 0.9609, 0.9531, 0.8516, 0.7344,
#                      0.6172, 0.5000, 0.4531, 0.2813, 0.1719, 0.1016, 0.0703,
#                      0.0625, 0.0547, 0.0000])
# ghia_u1    = np.array([1.00000, 0.84123, 0.78871, 0.73722, 0.68717, 0.23151, 0.00332 ,
#                       -0.13641, -0.20581, -0.21090, -0.15662, -0.10150, -0.06434, -0.04775,
#                       -0.04192, -0.03717, 0.00000])

# # # v(x, y=0.5)
# ghia_x_u2 = np.array([1.0000, 0.9688, 0.9609, 0.9531, 0.9453, 0.9063, 0.8594,
#                      0.8047, 0.5000, 0.2344, 0.2266, 0.1563, 0.0938, 0.0781,
#                      0.0703, 0.0625, 0.0000])
# ghia_u2    = np.array([0.0000, -0.05906, -0.07391, -0.08864, -0.10313, -0.16914, -0.22445,
#                       -0.24533, 0.05454, 0.17527, 0.17507, 0.16077, 0.12317, 0.10890, 0.10091,
#                       0.09233,  0.0000])

# # u(x=0.5, y) Re = 400
# ghia_y_u1 = np.array([1.0000, 0.9766, 0.9688, 0.9609, 0.9531, 0.8516, 0.7344,
#                      0.6172, 0.5000, 0.4531, 0.2813, 0.1719, 0.1016, 0.0703,
#                      0.0625, 0.0547, 0.0000])
# ghia_u1    = np.array([1.00000, 0.75837, 0.68439, 0.61756, 0.55892, 0.29093, 0.16256 ,
#                       0.02135, -0.11477, -0.17119, -0.32726, -0.24299, -0.14612, -0.10338,
#                       -0.09266, -0.08186, 0.00000])

# # v(x, y=0.5)
# ghia_x_u2 = np.array([1.0000, 0.9688, 0.9609, 0.9531, 0.9453, 0.9063, 0.8594,
#                      0.8047, 0.5000, 0.2344, 0.2266, 0.1563, 0.0938, 0.0781,
#                      0.0703, 0.0625, 0.0000])
# ghia_u2    = np.array([0.0000, -0.12146, -0.15663, -0.19254, -0.22847, -0.23827, -0.44993,
#                       -0.38598, 0.05186, 0.30174, 0.30203, 0.28124, 0.22965, 0.20920, 0.19713,
#                       0.18360,  0.0000])

#u(x=0.5, y) Re = 1000
ghia_y_u1 = np.array([1.0000, 0.9766, 0.9688, 0.9609, 0.9531, 0.8516, 0.7344,
                     0.6172, 0.5000, 0.4531, 0.2813, 0.1719, 0.1016, 0.0703,
                     0.0625, 0.0547, 0.0000])
ghia_u1    = np.array([1.00000, 0.65928, 0.57492, 0.51117, 0.46604, 0.33304, 0.18719 ,
                      0.05702, -0.06080, -0.10648, -0.27805, -0.38289, -0.29730, -0.22220,
                      -0.20196, -0.18109, 0.00000])

# v(x, y=0.5)
ghia_x_u2 = np.array([1.0000, 0.9688, 0.9609, 0.9531, 0.9453, 0.9063, 0.8594,
                     0.8047, 0.5000, 0.2344, 0.2266, 0.1563, 0.0938, 0.0781,
                     0.0703, 0.0625, 0.0000])
ghia_u2    = np.array([0.0000, -0.21388, -0.27669, -0.33714, -0.39188, -0.51550, -0.42665,
                      -0.31966, 0.02526, 0.32235, 0.33075, 0.37095, 0.32627, 0.30353, 0.29012,
                      0.27485,  0.0000])

# === 3. Interpola Ghia para os pontos do FreeFEM ===
ghia_interp_u1 = interp1d(ghia_y_u1, ghia_u1, kind='cubic', fill_value="extrapolate")
ghia_u1_interp = ghia_interp_u1(freefem_y)

ghia_interp_u2 = interp1d(ghia_x_u2, ghia_u2, kind='cubic', fill_value="extrapolate")
ghia_u2_interp = ghia_interp_u2(freefem_x)

# === 4. Plota comparações ===

# Perfil u(x=0.5)
plt.figure(figsize=(6, 6))
plt.plot(freefem_u1, freefem_y, label='FreeFEM', linewidth=2)
plt.plot(ghia_u1_interp, freefem_y, '--', label='Ghia et al. (interp)', linewidth=2)
plt.xlabel('u1 (velocidade horizontal)', fontsize=25)
plt.ylabel('y', fontsize=25)
plt.title('Perfil u1(x=0.5) Re=1000, t=20s', fontsize=30)
plt.legend(loc='lower right', fontsize=20)
plt.grid(True)
plt.tight_layout()

# Perfil v(y=0.5)
plt.figure(figsize=(6, 6))
plt.plot(freefem_x, freefem_u2, label='FreeFEM', linewidth=2)
plt.plot(freefem_x, ghia_u2_interp, '--', label='Ghia et al. (interp)', linewidth=2)
plt.xlabel('x', fontsize=25)
plt.ylabel('u2 (velocidade vertical)', fontsize=25)
plt.title('Perfil u2(y=0.5) Re=1000, t=20s', fontsize=30)
plt.legend(loc='lower right', fontsize=20)
plt.grid(True)
plt.tight_layout()

plt.show()
