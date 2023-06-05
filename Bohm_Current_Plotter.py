import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_excel('Bohm_Areas_0p64_0p7A.xlsx',index_col=None,header=0)

# Sort the data in ascending order, first by varied paramter bias and then by farday cup position
data.sort_values(by=["T_g", "T_e"], inplace=True)
T_e_grouped= data.groupby('T_e')
T_g_grouped = data.groupby('T_g')

# T_e_varied=T_e_grouped.groups.keys()
# T_g_varied=T_g_grouped.groups.keys()

fig, ax = plt.subplots()
fig2, ax2 = plt.subplots()

A_o_lims=[min(data["A_o"])*1e6,max(data["A_o"])*1e6]
D_o_lims=[min(data["D_o"])*1e3,max(data["D_o"])*1e3]
x_lims=[min(data["P"]), max(data["P"])]

for key,group in T_g_grouped:
    if key==600:
        plt_var=T_g_grouped.get_group(key)
        T_e_grouped2=plt_var.groupby('T_e')
        for key2,group2 in T_e_grouped2:
            print(key)
            group2["D_o"]=group2["D_o"]*1000
            group2["A_o"]=group2["A_o"]*1000000
            group2.plot("P","A_o",label=str(round(key2,1))+' eV', ax=ax, xlabel="Pressure [Torr]", ylabel="Extraction Grid Area [mm$^{2}$]",logx=True, logy=True, linestyle="-", marker='None')
            group2.plot("P","D_o",label=str(round(key2,1))+' eV', ax=ax2,xlabel="Pressure [Torr]", ylabel="Extraction Grid Diameter [mm]",logx=True, logy=True, linestyle="-", marker='None')
    ax.set_title("$T_{g}= 600 K$")
    ax.legend(title="$T_{e}= $")
    ax.plot([1e-5,1e-5],A_o_lims,linestyle=":",color="k")
    ax.set_ylim(A_o_lims)
    ax.set_xlim(x_lims)

    ax2.set_title("$T_{g}= 600 K$")
    ax2.legend(title="$T_{e}= $")
    ax2.plot([1e-5,1e-5],D_o_lims,linestyle=":",color="k")
    ax2.set_ylim(D_o_lims)
    ax2.set_xlim(x_lims)

fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

for key3,group3 in T_e_grouped:
    if key3==10.0:
        plt_var2=T_e_grouped.get_group(key3)
        T_g_grouped3=plt_var2.groupby('T_g')
        for key4,group4 in T_g_grouped3:
            print(key3)
            group4["D_o"]=group4["D_o"]*1000
            group4["A_o"]=group4["A_o"]*1000000
            group4.plot("P","A_o",label=str(round(key4,1))+' K', ax=ax3, xlabel="Pressure [Torr]", ylabel="Extraction Grid Area [mm$^{2}$]",logx=True, logy=True, linestyle="-", marker='None')
            group4.plot("P","D_o",label=str(round(key4,1))+' K', ax=ax4, xlabel="Pressure [Torr]", ylabel="Extraction Grid Diameter [mm]",logx=True, logy=True, linestyle="-", marker='None')
    ax3.set_title("$T_{e}=10.0$ eV")
    ax3.legend(title="$T_{g}= $")
    ax3.plot([1e-5,1e-5],A_o_lims,linestyle=":",color="k")
    ax3.set_ylim(A_o_lims)
    ax3.set_xlim(x_lims)

    ax4.set_title("$T_{e}=10.0$ eV")
    ax4.legend(title="$T_{g}= $")
    ax4.plot([1e-5,1e-5],D_o_lims,linestyle=":",color="k")
    ax4.set_ylim(D_o_lims)
    ax4.set_xlim(x_lims)
plt.show()