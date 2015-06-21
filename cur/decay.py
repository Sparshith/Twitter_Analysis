import csv
import sys
import collections

lis1=[]
lis2=[]
ind=[]

with open('twitter_stats.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	lis1.append(row[2])
    	lis2.append(row[1])

    	
del(lis1[0])
del(lis2[0])

count1= len(lis1)
lis3= set(lis2)
lis3= list(lis3)
count2= len(lis3)


for j in range(0,count2):
	#count=0
	indices=[]
	indices = [i for i, x in enumerate(lis2) if x == lis3[j]]
	print lis3[j],
	print ":",
	count3= len(indices)
	for k in range(0,count3):
		print lis1[indices[k]],
	print ""


