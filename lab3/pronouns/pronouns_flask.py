
"""
@app.route("/home/ubuntu/test")
def test():

    counts={"han":0, "hon":0, "den":0, "hen":0, "denne":0, "denna":0, "det":0, "count":0 }
    for filename in os.listdir("/home/ubuntu/Data/"):
        result = pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/"+filename, counts)

        for v2 in result.collect():
            counts=v2[1]

    print(counts)
    #result = json_results.delay()
#    result.wait()
    return result.wait()
"""
from pronouns_celery import pronoun_count_per_unique_tweet, all_pronoun_counts
#!flask/bin/python
from flask import Flask,jsonify
from celery import Celery
import json
import os
import re

from file import *

@app.route("/home/ubuntu/each", methods = ['GET'])
def each():

    counts={"han":0, "hon":0, "den":0, "hen":0, "denne":0, "denna":0, "det":0, "count":0 }
    for filename in os.listdir("/home/ubuntu/Data/"):
        #result = pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/"+filename, counts)

        #for v2 in result.collect():
        #    counts=v2[1]
        #counts= pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/" + filename, counts)
        result=  pronoun_count_per_unique_tweet.delay("/home/ubuntu/Data/" + filename, counts)
        counts = result.wait()
    return counts

@app.route("/home/ubuntu/all", methods = ['GET'])
def all():
    result=all_pronoun_counts.delay("/home/ubuntu/Data/")
    return result.wait()
    #return all_pronoun_counts("/home/ubuntu/Data/")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #all()
