from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def pronoun_count_per_unique_tweet(filename, counts, count):
    import re
    import sys
    import json

    pronouns=["han","hon", "den", "det", "denna", "denne", "hen"]
   
    f = open(file, "r")
    #for line in sys.stdin:
    for line in f.readlines():
         # remove ending character 
        line=line.replace("^M", "")
         # remove leading and trailing whitespace
        line = line.strip()

        if line=="":
            continue
        dictwit=json.loads(line)
       # print(dictwit['text'])

        try: 
            dictwit['retweeted_status']
        except KeyError:

            count+=1
            occurred=[]
            #remove comma, colon, dot, etc. with spaces via regex
            dictwit["text"]=re.sub("[':?;,/[.!\"(){}]", " ", dictwit["text"])
            # split the line into words
            words = dictwit['text'].split()
            for word in words:
            # write the results to STDOUT (standard output);
            # what we output here will be the input for the
            # Reduce step, i.e. the input for reducer.py
                #
            # tab-delimited; the trivial word count is 1
                if word.lower() in pronouns and not word.lower() in occurred:#2 den = 1 den in one tweet
                    occurred.append(word.lower())
                    #print ('%s\t%s' % (word.lower(), 1))
                    counts[word.lower()]+=1
    print('%s\t%s' % ("count", count)) 

    #for pronoun in pronouns:
    #    counts[pronoun]=counts[pronoun]/count
    print(counts)
    return counts, count
