#### Find the coordinates that are phyiscally closest to the coordinates given ####
import numpy as np

def hms2dec( hr, mins, secs ):
  hr2deg = 15 * hr
  mins2deg = 15 * mins/60 
  secs2deg = 15 * secs/3600
  decdeg = hr2deg + mins2deg + secs2deg
  return decdeg

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

def import_bss():
  res = []
  data = np.loadtxt('bss.dat', usecols=range(1, 7))
  for i, row in enumerate(data, 1):
    res.append((i, hms2dec(row[0], row[1], row[2]), dms2dec(row[3], row[4], row[5])))
  return res

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

def find_closest( compare, idealra, idealdec ):
  
  mindist = np.inf
  minid = None
  
  for id1, alph1, olimar1 in compare:
    angdist = angular_dist( alph1, olimar1, idealra, idealdec )
    if angdist < mindist:
      minid = id1
      mindist = angdist
  
  return minid, mindist

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
