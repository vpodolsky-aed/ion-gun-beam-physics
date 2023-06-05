###### Import Libraries ######
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

###### Define Constants ######
k_b=1.380649e-23; #J/k
m_D=3.34e-27; #kg---mass of deuterium atom, D
e=1.6e-19; #C---charge of an electron/proton
torr_2_pa=101325/760
eV_2_K=e/k_b;#11601.57 K/eV
pi=np.pi


###### Define Inputs ######
eta_conv=0.64; #Target/Assumed Neutral to Ion Conversion efficiency
I_b=.07; #A---Target Beam Current

p = np.logspace(-8, -3, 1000)  # Torr
T_g = np.array([300, 400, 500, 600, 700])  # K
T_e = np.array([0.1, 0.5, 1, 5, 10, 20, 50])  # eV - Target/Assumed electron temperature

# Create meshgrid for broadcasting
'''
need to use meshing to enable element-wise matrix multiplication  
'''
p_mesh, T_g_mesh, T_e_mesh = np.meshgrid(p, T_g, T_e, indexing='ij')

# Calculate variables using broadcasting
n_g = (p_mesh * torr_2_pa) / (k_b * T_g_mesh)
n_o = eta_conv * n_g
J_i = 0.6 * n_o * e * np.sqrt(k_b * T_e_mesh * eV_2_K / m_D)
A_o = I_b / J_i
D_o = np.sqrt(A_o * 4 / pi)

# Reshape the arrays and create the dataframe
'''
In terms of performance, D_o.ravel() is generally faster than D_o.flatten() because it avoids the overhead 
of creating a new copy of the array. However, it's important to note that if you intend to modify the flattened
array and want to keep the original array unchanged, D_o.flatten() should be used to ensure a new copy is created.
'''
df = pd.DataFrame({
    "P": p_mesh.ravel(),
    "T_g": T_g_mesh.ravel(),
    "T_e": T_e_mesh.ravel(),
    "n_g": n_g.ravel(),
    "n_o": n_o.ravel(),
    "J_i": J_i.ravel(),
    "A_o": A_o.ravel(),
    "D_o": D_o.ravel()
})
df.to_excel("Bohm_Areas_0p64_0p7A.xlsx")
'''
######Slow Method######
col_names = ["n_g", "n_o", "J_i", "A_o", "D_o"]
data = []

# # Perform Calculations
# for p_gas in p:
#     for t_gas in T_g:
#         n_g = p_gas * torr_2_pa / (k_b * t_gas)  # m^-3
#         n_o = eta_conv * n_g
#         for t_e in T_e:
#             J_i = 0.6 * n_o * e * np.sqrt(k_b * t_e * eV_2_K)
#             A_o = I_b / J_i  # You didn't specify the value for I_b
#             D_o = np.sqrt(A_o * 4 / pi)
#             data.append({"n_g": n_g, "n_o": n_o, "J_i": J_i, "A_o": A_o, "D_o": D_o})

# df = pd.DataFrame(data, columns=col_names)
'''