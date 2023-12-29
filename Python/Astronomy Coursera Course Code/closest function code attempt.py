# Write your find_closest function here
import numpy as np

#### NOTE THIS PART OF THE CODE WAS TO TRY TO PURELY FIND THE NUMERICALLY CLOSE VALUE ####
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
    liststep = []
    liststep.append( hms2dec(row[0], row[1], row[2]) )
    liststep.append( dms2dec(row[3], row[4], row[5]) )
    res.append(list(liststep))
  return res

def find_closest( compare, idealra, idealdec ):
  closest = []
  for i in range( len(compare) ):
    if abs(compare[i][0]) % abs( idealra ) == 0 :
      closest.append( compare[ i ] )
      break
    elif abs(compare[i][0]) % abs( idealra ) > 0 and abs(compare[i][0]) % abs( idealra ) < 2:
      closest.append( compare[ i ] )

  for j in range( len(closest) ):
    if abs(compare[j][1]) % abs( idealdec ) == 0 :
      closest = compare[ j ] 
      break
    elif abs(compare[j][1]) % abs( idealdec ) > 0 and abs(compare[j][1]) % abs( idealdec ) < 2:
      closest = compare[ j ]
  
  return closest

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  cat = import_bss()
  
  # First example from the question
  print(find_closest(cat, 175.3, -32.5))

  # Second example in the question
  print(find_closest(cat, 32.2, 40.7))
