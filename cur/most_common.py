import csv
import sys
import collections

#list to collect all words
words=[]
lis=[]


with open('twitter_data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        lis.append(row[1]) 
words=(''.join(lis)).split()
c=collections.Counter(words)
count= len(c)   
c=c.most_common(count)

lis2=[]


for i in range(0,count):
	print c[i][0],
	print ":",
	print c[i][1]
	
        

