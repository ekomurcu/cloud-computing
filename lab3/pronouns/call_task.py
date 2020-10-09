from tasks import add
count=0
counts={"han":0,"hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0}
result= pronoun_count_per_unique_tweet.delay("~/Data/20275995-d9e1-442c-bf33-7979aab6db8b", counts, count)
for v in result.collect():
    print(v)
