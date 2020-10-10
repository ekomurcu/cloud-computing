from pronouns import pronoun_count_per_unique_tweet
from pronouns import all_pronoun_counts
import os

counts={"han":0,"hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0, "count":0}
nof_nodes=8
total=0
nof_divide=0


for filename in os.listdir("/home/ubuntu/Data/"):
    total+= os.path.getsize("/home/ubuntu/Data/"+filename)/(1000**2)
    result= pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/"+ filename, counts)
    if total>200:
        total=0
        nof_divide+=1
    for v1 in result.collect():
        counts= v1[1]
    if nof_divide == nof_nodes:
        break
print(counts)

