# Write your crossmatch function here.
import numpy as np
import time

# function for calculating angular distance of 2 given coords
def angular_dist( alph1, olimar1, alph2, olimar2 ):
  absalph = abs( alph1 - alph2 )
  absolimar = abs( olimar1 - olimar2 )
  sinsquaredpart = np.sin( absolimar / 2 )**2
  coscossinsquaredpart = np.cos(olimar1)*np.cos(olimar2)*np.sin( absalph / 2 )**2
  underdabridge = np.sqrt( sinsquaredpart + coscossinsquaredpart )
  drad = 2*np.arcsin( underdabridge )
  return drad

# function for crossmatching and ouptputting information
def crossmatch( kit101, kit10too, maxsepdist ):
  start = time.perf_counter()
  total = 0
  matches = []
  no_matches = []
  maxrad = np.radians( maxsepdist )
  # convert arrays from deg to rad
  kit101 = np.radians( kit101 )
  kit10too = np.radians( kit10too )
  tiddykat = np.argsort( kit10too[:,1])
  tiddykitten = kit10too[ tiddykat ]
  # code for matching
  for id1, (alph1, olimar1) in enumerate( kit101 ):
    mindist = np.inf
    minid = None
    max_olimar = olimar1 + maxrad
    for id2, (alph2, olimar2) in enumerate( tiddykitten ):
      if olimar2 > max_olimar:
        break
      
      angdist = angular_dist( alph1, olimar1, alph2, olimar2 ) 
      if angdist < mindist:
        minid = tiddykat[ id2 ]
        mindist = angdist
      
      
    if mindist > maxrad:
      no_matches.append( id1 )
    else:
      matches.append(( id1 , minid, np.degrees( mindist )))
  total += time.perf_counter() - start
  return matches, no_matches, total


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # The example in the question
  cat1 = np.array([[180, 30], [45, 10], [300, -45]])
  cat2 = np.array([[180, 32], [55, 10], [302, -44]])
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)

  # A function to create a random catalogue of size n
  def create_cat(n):
    ras = np.random.uniform(0, 360, size=(n, 1))
    decs = np.random.uniform(-90, 90, size=(n, 1))
    return np.hstack((ras, decs))

  # Test your function on random inputs
  np.random.seed(0)
  cat1 = create_cat(10)
  cat2 = create_cat(20)
  matches, no_matches, time_taken = crossmatch(cat1, cat2, 5)
  print('matches:', matches)
  print('unmatched:', no_matches)
  print('time taken:', time_taken)
