import sys
import json
from collections import defaultdict


def sentiment(tweet, scores):
    if "text" not in tweet.keys():
        return 0
    if tweet.get("lang", "") !=  "en":
        return 0

    score = sum(map(lambda w: scores.get(w, 0), words(tweet)))
    return score


def create_sentiment_dict(afinnfile):
    afinnfile = open(afinnfile)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores


def words(tweet):
    return tweet["text"].split()


def main():
    sent_filename = sys.argv[1]
    tweet_filename = sys.argv[2]

    scores = create_sentiment_dict(sent_filename)
    tweets  = map(json.loads, open(tweet_filename).readlines())
    tweets = [tweet for tweet in tweets if "text" in tweet.keys()]

    positive_count = defaultdict(int)
    negative_count = defaultdict(int)

    all_words = set()
    for tweet in tweets:
        s = sentiment(tweet, scores)
        if s > 0:
            for w in words(tweet):
                positive_count[w] += 1
                all_words.add(w)
        elif s < 0:
            for w in words(tweet):
                negative_count[w] += 1
                all_words.add(w)

    new_sentiment = {}
    for word in all_words:
        if word in scores.keys():
            continue
        if negative_count[word] == 0:
            new_sentiment[word] = 100
        else:
            new_sentiment[word] = float(positive_count[word])/negative_count[word]
        print '%s %f' % (word, new_sentiment[word])


if __name__ == '__main__':
    main()
