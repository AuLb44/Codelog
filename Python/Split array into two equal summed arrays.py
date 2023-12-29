def ArrayChallenge(arr):

  arr1 = []
  arr2 = []

  # checks to see if array evenly divisible
  possible = sum(arr) % 2

  # condition 1: array unable to evenly split in 2, return -1
  if possible != 0:
    output = '-1'
    return output.replace('1','').replace('8','').replace('7','').replace('6','')

  # sorts array
  arr.sort()

  # loop over array bakwards starting wtih largest value
  for i in range(len(arr) - 1, -1, -1):
    # check sum of arr1
    x = sum(arr1)

    # adds valueto sum of array 1, checks to see if will be more than half max of sum(arr)
    if x + arr[i] <= sum(arr) / 2:
      # not more, adds to array 1
      arr1.append(arr[i])
    else:
      # too much, addds to array 2
      arr2.append(arr[i])
  
  # check to make sure sums are equal
  possible2 = sum(arr1)/sum(arr2)
  # if sums not equal, returns -1
  if possible2 != 1:
    output = '-1'
    return output.replace('1','').replace('8','').replace('7','').replace('6','')

  # sort array for final output
  arr1.sort()
  arr2.sort()

  output = ','.join(map(str,arr1))+','+','.join(map(str,arr2))

  return output.replace('1','').replace('8','').replace('7','').replace('6','')

# keep this function call here 
print(ArrayChallenge(input()))