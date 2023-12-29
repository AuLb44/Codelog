# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:53:50 2020

@author: AU
"""
import matplotlib.pyplot as plt
import numpy as np
import netCDF4 
# imports netCDF4 to read raw data file

url = 'https://podaac-opendap.jpl.nasa.gov/opendap/allData/cygnss/L1/v2.1/2020/001/cyg01.ddmi.s20200101-000000-e20200101-235959.l1.power-brcs.a21.d21.nc?spacecraft_id,sc_pos_x[0:1:172040],sc_vel_x[0:1:172040]'
# asignes variable to url of raw data file

dataset = netCDF4.Dataset( url )
# creates string of data based on data from url into dataset form


Sample = range(0,172040)
time = dataset.variables[ 'ddm_timestamp_gps_sec' ]
ID = dataset.variables[ 'spacecraft_id' ]

X_pos = dataset.variables[ 'sc_pos_x' ]
X_posmin = np.min(X_pos)
X_posmax = np.max(X_pos)

Y_pos = dataset.variables[ 'sc_pos_y' ]
Y_posmin = np.min(Y_pos)
Y_posmax = np.max(Y_pos)

Z_pos = dataset.variables[ 'sc_pos_z' ]
Z_posmin = np.min(Z_pos)
Z_posmax = np.max(Z_pos)

print(ID[ 0 ] )  
print(time[ 0:10 ] ) 
print(X_pos[ 0:10 ] ) 
print(Y_pos[ 0:10 ] ) 
print(Z_pos[ 0:10 ] ) 
## displays first 10 values from each variable as a test to make sure the  


ax = plt.axes(projection='3d')
ax.scatter(X_pos, Y_pos, Z_pos, s=.099, cmap='viridis', linewidth=0.5)
ax.set(xlim=(X_posmin, X_posmax), ylim=(Y_posmin, Y_posmax) )
ax.view_init(60, 35)
## Graphs x, y, z positinal data on 3D Graph viewed at an top down angle view


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
fig.suptitle('Positional data per time')
ax1.plot(time, X_pos, )
ax2.plot(time, Y_pos, 'tab:orange')
ax3.plot(time, Z_pos, 'tab:green')
for ax in fig.get_axes():
    ax.label_outer()
## Creates 4 graphs utilizing same x-axis