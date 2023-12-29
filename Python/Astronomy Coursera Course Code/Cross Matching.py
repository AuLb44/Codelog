#### find the index of the matches of the two data sets where they are roughly same position ####
import numpy as np

# Function for converting RA time to degrees
def hms2dec( hr, mins, secs ):
  hr2deg = 15 * hr
  mins2deg = 15 * mins/60 
  secs2deg = 15 * secs/3600
  decdeg = hr2deg + mins2deg + secs2deg
  return decdeg

# Function for converting dec degrees to degrees
def dms2dec( deg, amins, asecs ):
  if deg >= 0:
    mins2deg = amins/60 
    secs2deg = asecs/3600
    decdeg = deg + mins2deg + secs2deg
  else:
    mins2deg = -1*(amins/60) 
    secs2deg = -1*(asecs/3600)
    decdeg = deg + mins2deg + secs2deg
  return decdeg

# function for reading bss data to a list of touples
def import_bss():
  res = []
  data = np.loadtxt('bss.dat', usecols=range(1, 7))
  for i, row in enumerate(data, 1):
    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return res

# function for reading super data to a list of touples
def import_super():
  importantinfo = np.loadtxt('super.csv', delimiter=',', skiprows=1, usecols=(0, 1))
  res = []
  for i, row in enumerate(importantinfo, 1):
    res.append((i, row[0], row[1]))
  return res 

# function for calculating angular distance of 2 given coords
def angular_dist( alph1, olimar1, alph2, olimar2 ):
  radalph1 = np.radians( alph1 )
  radalph2 = np.radians( alph2 )
  radolimar1 = np.radians( olimar1 )
  radolimar2 = np.radians( olimar2 )
  absalph = abs( radalph1 - radalph2 )
  absolimar = abs( radolimar1 - radolimar2 )
  sinsquaredpart = np.sin( absolimar / 2 )**2
  coscossinsquaredpart = np.cos(radolimar1)*np.cos(radolimar2)*np.sin( absalph / 2 )**2
  underdabridge = np.sqrt( sinsquaredpart + coscossinsquaredpart )
  drad = 2*np.arcsin( underdabridge )
  d = np.degrees( drad )
  return d

# function for taking a list of tuples and 2 data points and comparing to find one at the closest distance to given coords
def find_closest( compare, idealra, idealdec ): 
  mindist = np.inf
  minid = None  
  for id1, alph1, olimar1 in compare:
    angdist = angular_dist( alph1, olimar1, idealra, idealdec )
    if angdist < mindist:
      minid = id1
      mindist = angdist 
  return minid, mindist

# function for crossmatching and ouptputting information
def crossmatch( bs, supe, maxsepdist ):
  matches = []
  no_matches = []
  for i in bs:
    index,idealra, idealdec = i
    matchposs, mindist = find_closest( supe, idealra, idealdec )
    if mindist > maxsepdist:
      no_matches.append( i[0] )
    else:
      matchinfo = i[0], matchposs, mindist
      matches.append( matchinfo )
  return matches, no_matches

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  bss_cat = import_bss()
  super_cat = import_super()

  # First example in the question
  bss_cat = import_bss()
  super_cat = import_super()
  max_dist = 40/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
  
  # Second example in the question
  max_dist = 5/3600
  matches, no_matches = crossmatch(bss_cat, super_cat, max_dist)
  print(matches[:3])
  print(no_matches[:3])
  print(len(no_matches))
