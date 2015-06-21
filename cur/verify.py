import csv

lis1=[]

with open('twitter_data.csv', 'rb') as f:
	reader= csv.reader(f)
	for row in reader:
		lis1.append(row[0])

count1= len(lis1)
lis1= set(lis1)
count2= len(lis1)
print count1
print count2
