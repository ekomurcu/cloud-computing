#venv
#FLASK_APP=pronouns_fsk_celery.py flask run --host=0.0.0.0
#venv
#celery -A pronouns_flask_celery.celery worker -l info
#curl -i http://<>:5000/home/ubuntu/workplace


from flask import Flask,jsonify
from celery import Celery
import json
import os
import re

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

app = Flask(__name__)
app.config.update(
        CELERY_BROKER_URL='amqp://ekomurcu:Bjk1995030507@192.168.2.7:5672/192.168.2.122',
    CELERY_RESULT_BACKEND='rpc'
)


celery = make_celery(app)

app = Flask(__name__)


@app.task
def pronoun_count_per_unique_tweet(filename, counts):
    import re
    import sys
    import json

    pronouns=["han","hon", "den", "det", "denna", "denne", "hen"]

    f = open(filename, "r")
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

            counts["count"]+=1
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
    #print('%s\t%s' % ("count", count))

    #for pronoun in pronouns:
    #    counts[pronoun]=counts[pronoun]/count
    #print(counts)
    #return (counts, count)
    return counts

@app.task
def all_pronoun_counts(directory_path):
    import os
    counts={"han":0,"hon":0, "den":0, "det":0, "denna":0, "denne":0, "hen":0, "count":0 }
    for each in os.listdir(directory_path):
        counts= pronoun_count_per_unique_tweet(directory_path+ each, counts)
    for pronoun in counts.keys():
        counts[pronoun]= counts[pronoun]/float(counts["count"])

    return counts



@app.route("/home/ubuntu/workplace")
def home():

    counts={"han":0, "hon":0, "den":0, "hen":0, "denne":0, "denna":0, "det":0, "count":0 }
    for filename in os.listdir("/home/ubuntu/Data/"):
        result = pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/"+filename, counts)

        for v2 in result.collect():
            counts=v2[1]

    print(counts)
    ^#result = json_results.delay()
#    result.wait()
    return result.wait()
