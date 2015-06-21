import requests
import csv
import json

tweets=[] #list to hold all the tweets

with open('twitter_data.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        tweets.append(row[1]) 

del(tweets[0])

tweets = json.dumps(tweets) #encoding
r = requests.post("http://sentiment.vivekn.com/api/batch/", tweets)

r_decoded= json.loads(r.text) #decoding

i=0

for elements in r_decoded:
	print elements["result"],
	print ",",
	print elements["confidence"]
	

