import csv
import sys
from pprint import pprint
csv.register_dialect('pik',delimiter='|')
'''
with open('bikes.csv',mode='w') as f:
    #spamreader = csv.reader(f, delimiter=' ', quotechar='|')
    #for row in spamreader:
    #    print(', '.join(row))    
    spamwriter=csv.writer(f,quoting=csv.QUOTE_NONNUMERIC)
    spamwriter.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
    for i in range(3):
        row=(
            i+1,
            chr(ord('a')+1),
            '08/{:02d}/07'.format(i+1),
            i*2,)
        spamwriter.writerow(row)
'''




with open('bikes.csv',mode='r') as f:
    reader=csv.DictReader(f)
    trip=next(reader)
    pprint(trip)


        
            
