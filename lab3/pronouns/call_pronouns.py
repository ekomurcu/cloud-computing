from pronouns import pronoun_count_per_unique_tweet
from pronouns import all_pronoun_counts
count1=0
counts1={"han":0,"hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0}
result= pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/20275995-d9e1-442c-bf33-7979aab6db8b", counts1, count1)
for v1 in result.collect():
    print(v1)

result_all=all_pronoun_counts.delay("/home/ubuntu/Data/")

for v2 in result_all.collect():
    print(v2)

