# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 13:53:50 2020

@author: AU
"""

import numpy as np
import netCDF4 
from time import process_time
import math

url = 'https://podaac-opendap.jpl.nasa.gov/opendap/allData/cygnss/L1/v2.1/2020/001/cyg01.ddmi.s20200101-000000-e20200101-235959.l1.power-brcs.a21.d21.nc?spacecraft_id,ddm_timestamp_gps_sec[0:1:172040],sc_pos_x[0:1:172040],sc_pos_y[0:1:172040],sc_pos_z[0:1:172040],sc_vel_x[0:1:172040],sc_vel_y[0:1:172040],sc_vel_z[0:1:172040],sc_roll[0:1:172040],sc_pitch[0:1:172040],sc_yaw[0:1:172040],sc_lat[0:1:172040],sc_lon[0:1:172040],sc_alt[0:1:172040]'
# asignes variable to url of raw data file

dataset = netCDF4.Dataset( url )
# creates string of data based on data from url into dataset form

Sample = range(0,172040)
ID = dataset.variables[ 'spacecraft_id' ]
time = dataset.variables[ 'ddm_timestamp_gps_sec' ]

X_pos = dataset.variables[ 'sc_pos_x' ]
X_posmin = np.min(X_pos)
X_posmax = np.max(X_pos)

Y_pos = dataset.variables[ 'sc_pos_y' ]
Y_posmin = np.min(Y_pos)
Y_posmax = np.max(Y_pos)

Z_pos = dataset.variables[ 'sc_pos_z' ]
Z_posmin = np.min(Z_pos)
Z_posmax = np.max(Z_pos)

X_vel = dataset.variables[ 'sc_vel_x' ]
X_velmin = np.min(X_vel)
X_velmax = np.max(X_vel)

Y_vel = dataset.variables[ 'sc_vel_y' ]
Y_velmin = np.min(Y_vel)
Y_velmax = np.max(Y_vel)

Z_vel = dataset.variables[ 'sc_vel_z' ]
Z_velmin = np.min(Z_vel)
Z_velmax = np.max(Z_vel)

Roll = dataset.variables[ 'sc_roll' ]
Rollmin = np.min(Roll)
Rollmax = np.max(Roll)

Pitch = dataset.variables[ 'sc_pitch' ]
Pitchmin = np.min(Pitch)
Pitchmax = np.max(Pitch)

Yaw = dataset.variables[ 'sc_yaw' ]
Yawmin = np.min(Yaw)
Yawmax = np.max(Yaw)

Lat = dataset.variables[ 'sc_lat' ]
Lon = dataset.variables[ 'sc_lon' ]
Alt = dataset.variables[ 'sc_alt' ]

t1 = process_time( )

a = np.array( X_vel[0:172040] )
b = a**2
c = np.array( Y_vel[0:172040] )
d = c**2
f = np.array( Z_vel[0:172040] )
g = f**2
u = b + d + g
R = np.sqrt( u )
#creates an array from the variable. Each value in the array is squared
#summed with the corresponding value in the each dimension and square root of 
#the sum is placed in a new array. Creating a magnitude array

t2 = process_time( )

t = t2-t1
print( 'processing time =', t, 'seconds' )
print( R[0:4] )