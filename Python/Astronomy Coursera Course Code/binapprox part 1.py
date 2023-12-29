# Write your median_bins and median_approx functions here.
import numpy as np
#### LEGACY CODE FROM ATTEMPT ####
# def median_bins( name, B ):
#   # use Numpy functions to calculate mean and std
#   mean = np.mean( name )
#   std = np.std( name )
#   # calc the upper and lower bin bounds
#   minval = mean - std
#   maxval = mean + std
#   # creates bin for bad/good data
#   mintrash = []
#   gooddata = []
#   #create for loop and if statement to begin binning values
#   for i in range( len(name) ):
#     if name[i] < minval:
#       mintrash.append( name[i] )
#     else: 
#       gooddata.append( name[i] )
#   # set the bin width value
#   binwidth = ( 2 * std ) / B
#   # make bins for counting values
#   bins = []
#   bincounts = []
#   for i in range(B):
#     if minval <= gooddata[i] < (minval + binwidth):
#       bins.append( gooddata[i] )
#       bincounts.append( len( bins ) )
#     elif (minval + binwidth) < gooddata[i] < (minval + (binwidth * i ) ):
#       bins.append( gooddata[i] )
#       bincounts.append( len( bins ) ) 
#   return (mean, std, len( mintrash), bincounts )

def median_bins( values, B ):
  # use Numpy functions to calculate mean and std
  mean = np.mean( values )
  std = np.std( values )
  # calc the upper and lower bin bounds
  minval = mean - std
  maxval = mean + std
  # creates bin for bad/good data
  mintrash = 0
  bins = np.zeros(B)
  # set the bin width value
  binwidth = ( 2 * std ) / B
  #create for loop and if statement to begin binning values
  for value in values:
    if value < minval:
      mintrash += 1
    elif value < maxval: 
      gooddata = int(( value - minval)/binwidth)
      bins[ gooddata ] += 1
  return (mean, std, mintrash, bins )

def median_approx( values, B ):
  # intinally callilng data from prior function
  mean, std, mintrash, bins = median_bins(values, B)
  # sets up number of values and midpoint length
  N = len( values )
  midpoint = ( N + 1) / 2
  # counts how many positions over to midpoint
  count = mintrash
  for i, bincount in enumerate(bins):
    count += bincount
    if count >= midpoint:
      # Stop when the cumulative count exceeds the midpoint
      break
  binwidth = 2 * std / B
  median = mean - std + binwidth * ( i + 0.5 )
  return median

# You can use this to test your functions.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your functions with the first example in the question.
  print(median_bins([1, 1, 3, 2, 2, 6], 3))
  print(median_approx([1, 1, 3, 2, 2, 6], 3))

  # Run your functions with the second example in the question.
  print(median_bins([1, 5, 7, 7, 3, 6, 1, 1], 4))
  print(median_approx([1, 5, 7, 7, 3, 6, 1, 1], 4))
