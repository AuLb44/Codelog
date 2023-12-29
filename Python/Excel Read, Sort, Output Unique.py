import pandas as pd
from collections import OrderedDict as OD


df1 = pd.read_excel("[INSERT DRIVE LOCATION HERE]")
df2 = pd.read_excel("[INSERT DRIVE LOCATION HERE]")

print(len(df1))
print(len(df2))

SKU2 = list(OD.fromkeys(df1))
SKU1 = list(OD.fromkeys(df2))


SKUList = df1

SKUsUnchecked = []
MissingSKU = []
k = 0

print("RUNNING")

for j in SKUList:
    if j in df2:
        SKUsUnchecked.append(j)
    else: 
        ''
    k = +1

print(SKUsUnchecked)
print(len(SKUsUnchecked))

listToStr1 = ' '.join(map(str, SKUsUnchecked))

file1 = open("SKUsUnchecked.txt","a")
file1.write(listToStr1)
file1.close()

print("donzo")
