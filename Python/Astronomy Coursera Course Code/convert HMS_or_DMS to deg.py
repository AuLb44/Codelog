#### Convert hms and dms to degrees ####

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

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The first example from the question
  print(hms2dec(23, 12, 6))

  # The second example from the question
  print(dms2dec(22, 57, 18))

  # The third example from the question
  print(dms2dec(-66, 5, 5.1))
