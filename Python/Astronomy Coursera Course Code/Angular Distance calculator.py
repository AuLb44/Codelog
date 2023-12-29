#### Angular distance calculator ####
import numpy as np
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


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  print(angular_dist(21.07, 0.1, 21.15, 8.2))

  # Run your function with the second example in the question
  print(angular_dist(10.3, -3, 24.3, -29))
