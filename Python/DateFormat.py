from datetime import datetime
import csv 

def datesort(data):
    return data['InputDate']
    
dataset = []

with open('table.csv','r') as Data:
    reader = csv.reader(Data,delimiter=',',quotechar='"')
    for row in reader:
        Date = ''
        for index,field in enumerate(row):
            if "GMT" in field:
                """ Thu Oct 19 2023 13:29:19 GMT-0400 (Eastern Daylight Time) """
                """ 0123456789 """
                Date = field[field.index(' ')+1:field.index(':')-2].strip()
                Date = datetime.strptime(Date,'%b %d %Y').date()
        x = {
            "InputDate": str(Date)
        }
        dataset.append(x)

print(dataset)       
dataset.sort(key=datesort,reverse=True)
print(dataset)