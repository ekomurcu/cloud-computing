from pronouns import all_pronoun_counts
from pronouns import pronoun_count_per_unique_tweet as tw
import os
#result_all=all_pronoun_counts.delay("/home/ubuntu/Data/")

counts={"han":0, "hon":0, "den":0, "hen":0, "denne":0, "denna":0, "det":0, "count":0 }
for filename in os.listdir("/home/ubuntu/Data/"):
    result = tw.delay("/home/ubuntu/Data/"+filename, counts)

    for v2 in result.collect():
        counts=v2[1]

print(counts)
