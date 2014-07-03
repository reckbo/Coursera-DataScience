import sys
import json


def create_sentiment_dict(afinnfile):
    afinnfile = open(afinnfile)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores

def sentiment(tweet, scores):
    if "text" not in tweet.keys():
        return 0
    if tweet.get("lang", "") !=  "en":
        return 0

    words = tweet["text"].split(" ")
    score = sum(map(lambda w: scores.get(w, 0), words))
    return score

def main():
    sent_filename = sys.argv[1]
    tweet_filename = sys.argv[2]
    scores = create_sentiment_dict(sent_filename)
    tweets  = map(json.loads, open(tweet_filename).readlines())
    for tweet in tweets:
        print sentiment(tweet, scores)

if __name__ == '__main__':
    main()
