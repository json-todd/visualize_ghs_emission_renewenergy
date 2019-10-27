import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

data = pd.ExcelFile('EnergyData.xlsx')

fuel = data.parse('Fuel')
plant = data.parse('Plant')
infras = data.parse('Infrastructure')
total = data.parse('Total'  )

sns.set(rc={'figure.figsize':(20,8)})
#sns.set(rc={'figure.figsize':(11.7,8.27)})
#sns.set_style("whitegrid")

color_dict = dict({
        'Direct Combustion': 'DarkOrange' ,
        'Co-combustion': 'IndianRed' ,
        'Gasification': 'DarkGray' ,
        'Wind': 'LightCyan' ,
        'Solar PV': 'Yellow', 
        'Hydro': 'DodgerBlue' })

plt.subplot(1,4,1)
ax1 = sns.stripplot(data = fuel, jitter = True, size = 10, linewidth = 1.5, palette = color_dict)
#ax1.set_xticklabels(ax1.get_xticklabels(), fontsize = 9)
ax1.set_xticklabels([])
plt.ylabel('kg CO2 eq/MWh electricity output', fontsize = 20, labelpad = 20)
plt.title('Emissions by Fuel Provision stage', fontsize = 'x-large', pad = 30)
#plt.show()

plt.subplot(1,4,2)
ax2 = sns.stripplot(data = plant, jitter = True, size = 10, linewidth = 1.5, palette = color_dict)
#ax2.set_xticklabels(ax2.get_xticklabels(), rotation=60, horizontalalignment = 'right')
ax2.set_xticklabels([])
#plt.ylabel('kg CO2 eq/MWh electricity output', fontsize = 'x-large')
plt.title('Emissions by Plant Operation stage', fontsize = 'x-large', pad = 30)
#plt.show()

plt.subplot(1,4,3)
ax3 = sns.stripplot(data = infras, jitter = True, size = 10, linewidth = 1.5, palette = color_dict)
#ax3.set_xticklabels(ax3.get_xticklabels(), rotation=60, horizontalalignment = 'right')
ax3.set_xticklabels([])
#plt.ylabel('kg CO2 eq/MWh electricity output', fontsize = 'x-large', labelpad = 20)
plt.title('Emissions by Plant Construction & Decommission stages', fontsize = 'x-large',pad = 30)
#plt.show()

plt.subplot(1,4,4)
ax4 = sns.boxplot(data = total, palette = color_dict)
#ax4.set_xticklabels(ax4.get_xticklabels(), rotation=60, horizontalalignment = 'right')
ax4.set_xticklabels([])
#plt.ylabel('kg CO2 eq/MWh electricity output', fontsize = 'x-large')
plt.title('Total Life Cycle Emissions', fontsize = 'x-large',pad = 30)


plt.tight_layout()
plt.show()
