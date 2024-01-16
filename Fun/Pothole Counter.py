# Python code Potholes
from random import randint

# Practice Test
Test1 = ['0110011011100', 7 ]               # Should be 5
Test2 = ['001111100', 4 ]                   # Should be 3
Test3 = ['000000', 5 ]                      # Should be 0
Tests = [Test1,Test2,Test3]                 # Grouped for loop testing

# Random Case Generator
def CaseCreator():
    S = ''                                  # String Initialize
    for x in range(1,randint(1,99999)):     # loop over random leng
        number = str(randint(0,1))          # generates 1 or 0 
        S += number                         # appends number to string
    B = randint(1,99999)                    # generates random value for B
    return(S,B)                             # returns S and B


# function
def Potholes(S,B):
    
    # Initialize Variables
    i = []                                  # Consectuive Pothole Listing
    j = 0                                   # Pothole Count
    
    for k in S:                             # loops over S string
        if k == '1':                        # Checks if pothole
            j += 1                          # if pothole, adds to count
        else:
            if j > 0:                       # if pothole count is more than 0, append
                i.append(j)                 # appends pothole count to Consecutive Pothole Listing
            j = 0           
    if j > 0:                               # double checks pothole count is more than 0 in case ending count not added
        i.append(j)                         # appends pothole count to Consecutive Pothole Listing
        
    i = sorted(i,reverse=True)              # reverse the list from most to least
    
    fixed = 0                               # Initilize count fixed
    for count in i:                         # Loop over list consecutive count val
        cost = count + 1                    # Calculates count fix whole value
        if B > cost:                        # If cost is less than budget
            B -= cost                       # Subtract Cost from buget
            fixed += count                  # Add count to fixed
        elif B > 0:                        
            fixed += B%cost - 1             # else takes finds remainder of cost in budget and subtracts one to get number of potholes can be fixed with rest of budget
        print("Count", count)
        print("cost count", cost)
        print("fixed count",fixed) 
        print("Budget left",B)
        print("\n")  
    return(fixed)                           # return fixed

# Run Test Cases
""" for test in Tests:
    print("The number of potholes fixed is: ", Potholes(test[0],test[1]) ) """


""" # ask user for number of random cases to run
CaseNum = int(input("how many cases do you want to run?\n"))
# run cases
for run in range(0,CaseNum):
    case = CaseCreator()
    print("Budget: ",case[1])
    print("The number of potholes fixed is: ", Potholes(case[0],case[1]) ) """
    
    
#### User Manual Entry Section ####
# ask user for street string and Budget
String = input("Please Enter String\n")
Budget = int(input("Please Enter Whole value budget\n"))
print("The number of potholes fixed is: ", Potholes(String,Budget) )
