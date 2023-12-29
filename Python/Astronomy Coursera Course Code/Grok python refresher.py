#### Python Refresher ####

# print statement
print( 'hello world' )

## Print names ##
# Write your greet function definition below:
def greet(name):
    return 'Hello, ' + name + '!' 
# Any code inside the if statement will be ignored by the automarker.
# Put your test code in here, since it will be run by clicking Run or Terminal.
if __name__ == '__main__':
  print(greet('World'))
  print(greet('Grok'))
  print(greet('123'))


## Calcualte mean function ##
# Write your calculate_mean function here.
def calculate_mean( name ):
  return ( sum( name ) ) / len( name )


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calculate_mean` function with examples:
  mean = calculate_mean([1,2.2,0.3,3.4,7.9])
  print(mean)


## Create tuple of median and mean for random array of numbers ##
# Write your list_stats function here.
import numpy as np

def list_stats( name ):
  
  if len( name ) % 2 == 0:
    mid = len( name ) // 2
    name.sort()
    median = ( name[ mid - 1 ] + name[ mid ] ) / 2
    mn = np.round_( np.mean( name ),  2 )
    tup =( median, mn  )
  else:
    mid = len( name ) // 2
    name.sort()
    median = name[ mid ] 
    mn = np.round( np.mean( name ), 2 )
    tup =( median, mn  )
  return tup 

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your function with the first example in the question.
  m = list_stats([1.3, 2.4, 20.6, 0.95, 3.1, 2.7])
  print(m)

  # Run your function with the second example in the question
  m = list_stats([1.5])
  print(m)
  
  
## Time trial for mean vs calc ##
import numpy as np
import statistics
import time

def time_stat(func, size, ntrials):
  # the time to generate the random array should not be included
  total = 0
  
  for i in range( ntrials ):
    data = np.random.rand(size)
  # modify this function to time func with ntrials times using a new random array each time
    start = time.perf_counter()
    res = func(data)
    total += time.perf_counter() - start
  # return the average run time
  return total/ntrials

if __name__ == '__main__':
  print('{:.6f}s for statistics.mean'.format(time_stat(statistics.mean, 10**5, 10)))
  print('{:.6f}s for np.mean'.format(time_stat(np.mean, 10**5, 1000)))


## check size of objects in python storage ##
import sys

a = 3
b = 3.123
c = [a, b]
d = [ ]
for obj in [a, b, c, d]:
  print(obj, sys.getsizeof(obj))
  

# for arrays
import numpy as np

a = np.array([])
b = np.array([1, 2, 3])
c = np.zeros(10**6)

for obj in [a, b, c]:
  print('sys:', sys.getsizeof(obj), 'np:', obj.nbytes)
  
  
a = np.zeros(5, dtype=np.int32)
b = np.zeros(5, dtype=np.float64)

for obj in [a, b]:
  print('nbytes         :', obj.nbytes)
  print('size x itemsize:', obj.size*obj.itemsize)
