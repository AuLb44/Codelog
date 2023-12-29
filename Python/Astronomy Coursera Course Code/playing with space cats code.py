#### CODE BAD AND NOTE ENTIRELY SURE WHY ####
# 
# # Write your import_bss function here.
# import numpy as np
# 
# def hms2dec( hr, mins, secs ):
#   hr2deg = 15 * hr
#   mins2deg = 15 * mins/60 
#   secs2deg = 15 * secs/3600
#   decdeg = hr2deg + mins2deg + secs2deg
#   return decdeg
# 
# def dms2dec( deg, amins, asecs ):
#   if deg >= 0:
#     mins2deg = amins/60 
#     secs2deg = asecs/3600
#     decdeg = deg + mins2deg + secs2deg
#   else:
#     mins2deg = -1*(amins/60) 
#     secs2deg = -1*(asecs/3600)
#     decdeg = deg + mins2deg + secs2deg
#   return decdeg
# 
# def import_bss( bigassdata ):
#   res = []
#   importantinfo = np.loadtxt('bss.dat', usecols = range( 1, 7 )
#   for i, row in enumerate( importantinfo , 1):
#     res.append(( i, hms2dec( row[ 0 ], row[ 1 ], row[ 2 ] ), dms2dec( row[ 3 ], row[ 4 ], row[ 5 ] ) ) )
#   return res
# 
# def import_super( biggerassdata ):
#   
#   importantinfo = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
#   
#   return importantinfo
# 
# 
# # You can use this to test your function.
# # Any code inside this `if` statement will be ignored by the automarker.
# if __name__ == '__main__':
#   # Output of the import_bss and import_super functions
#   bss_cat = import_bss( )
#   super_cat = import_super( )
#   print(bss_cat)
#   print(super_cat)
