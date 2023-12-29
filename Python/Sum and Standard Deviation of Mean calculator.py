# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 14:09:18 2020

@author: AU
"""




import numpy as np
import netCDF4 as BIG


# file = r'C:\Users\albee\OneDrive\Documents\Python Scripts\sample.nc4'
# Data = BIG.Dataset( file )
# U = Data.variables[ 'sc_pos_x' ]

# x = ( np.array( U ) )
# # creates array from data set

# X_max = np.max( x )
# X = (x - np.min(x))/np.ptp(x)
# # finds max and normalizes data, only necessary for this case because data set is robust

# X_bar = sum( X )
# # sums values of array X

# n = len( X ) 
# # counts number of items in array X

# Y = [ u - X_bar for u in X ]
# # Takes values of array and subtracts X_bar from each value of array X

# delta = np.sqrt( np.divide( sum( np.square( Y ) )  , n*(n-1) ) ) 
# print( delta )

# More Concise code for general usage
def Stadard_Deviation_Calculator():
    X = ( np.array( "Data" ) 
    X_bar = sum(X)
    delta = np.sqrt(np.divide(sum(np.square([ u - X_bar for u in X ])),len(X)*(len(X)-1))) 
