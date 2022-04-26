# -*- coding: utf-8 -*-
# -*- coding: iso-8859-1 -*-
# =====================================================================>
# By CT(T) ALANA April 1, 2022
# =====================================================================>

# Import libraries
import datetime, time
import os, sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Taking the temperature on the ICE X dpns30!
os.system("sshpass -p '@dmd@30' ssh root@10.13.100.30 'cmcexec sensor' > temperature_dpns30.txt")

# Replacing the blank spaces for nothing; replacing the " | " for "Comma" and delering the firts line Rack
os.system("cat temperature_dpns30.txt | sed 's, ,,g' | sed 's,|,\,,g' | sed '/rack/d' > new_temperature_dpns30.txt")

# Reading the CSV and creating several headers for each column! 
df = pd.read_csv('new_temperature_dpns30.txt', sep = ',', names=['Racks', 'Temp', 'Units', 'x4', 'x5', 'x6', 'x7', 'x8', 'x9', 'x10'])

# Creating a new DataFrame with the CMCInlet(front) and CMCOutlet(back) temperature! 
# The original DataFrame was created being String, but we changed it in to numbers using Float at the begining!
Racks  = ['CMC-R1i0c', 'CMC-R1i1c', 'CMC-R1i2c', 'CMC-R1i3c']
CMCInlet  = [float(df.iloc[1,1]), float(df.iloc[88,1]), float(df.iloc[175,1]), float(df.iloc[262,1])]
CMCOutlet = [float(df.iloc[2,1]), float(df.iloc[89,1]), float(df.iloc[176,1]), float(df.iloc[263,1])]

new_df = pd.DataFrame(list(zip(CMCInlet, CMCOutlet)), index = Racks, columns = ['CMCInlet', 'CMCOutlet'])
print(new_df)

# Ploting the Graphic
x = Racks
print(type(x))
y1 = CMCInlet
print(y1)
y2 = CMCOutlet

plt.plot(x,y1, label = 'CMCInlet',  marker='.', markersize=10)
plt.plot(x,y2, label = 'CMCOutlet',  marker='.', markersize=10)
plt.title('Temperature of CMC-Racks | ICE X', fontdict={'fontsize' : 16})
plt.xlabel('')
plt.ylabel('Temperature (ºC)')
plt.legend()

#fig, ax = plt.subplots(figsize=(12,6)
#ax = plt.gca()
#ax.set_ylim([0,25])
#plt.ylim((15.0,30.0))
plt.show()
plt.savefig('TempICEX.png')


fig, ax = plt.subplots()
Racks  = ('CMC-R1i0c', 'CMC-R1i1c', 'CMC-R1i2c', 'CMC-R1i3c')
hbar = ax.barh(Racks, y1)
ax.set_yticks(Racks)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Temperature (ºC)')
ax.set_title('Temperature of CMC-Racks | ICE X')
# Label with given captions, custom padding and annotate options
#ax.bar_label(hbars, fmt='%.2f')
#ax.set_xlim(right=30)
plt.show()
# Ploting the Second Graphic
#x1 = CMCInlet
#x2 = CMCOutlet
#y = Racks

#fig, ax = plt.subplots()
#ax.bar(x, y1, width=1, edgecolor="white", linewidth=0.7)
#ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#       ylim=(0, 8), yticks=np.arange(1, 8))


#ax.stem(x, y)

#ax.set(xlim=(), ylim=())
#plt.show()



# Another way to visualize the Data Frame !!!!!! Just if you want!
# Creating a new Data Frame with the value of CMC Inlet (front) temperature!
#new_df_inlet = pd.DataFrame({'CMC-Inlet-R1i0c' : [df.iloc[1,1]], 
#                             'CMC-Inlet-R1i1c' : [df.iloc[88,1]], 
#                             'CMC-Inlet-R1i2c' : [df.iloc[175,1]], 
#                             'CMC-Inlet-R1i3c' : [df.iloc[262,1]]}, index = ['Temperature (ºC)'])
#print(new_df_inlet)

# Creating a new Data Frame with the value of CMC Outlet (back) temperature! 
#new_df_Outlet = pd.DataFrame({'CMC-Outlet-R1i0c' : [df.iloc[2,1]],
#                              'CMC-Outlet-R1i1c' : [df.iloc[89,1]],
#                              'CMC-Outlet-R1i2c' : [df.iloc[176,1]],
#                              'CMC-Outlet-R1i3c' : [df.iloc[263,1]]}, index = ['Temperature (ºC)'])
#print(new_df_Outlet)

