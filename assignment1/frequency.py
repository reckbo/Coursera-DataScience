import sys
import json
from collections import defaultdict


def words(tweet):
    return tweet["text"].split()


def tweets(filename):
    tweets  = map(json.loads, open(filename).readlines())
    return [tweet for tweet in tweets if "text" in tweet.keys() and tweet["lang"] == "en"]


def main():
    tweet_filename = sys.argv[1]

    count = defaultdict(int)
    total = 0
    for tweet in tweets(tweet_filename):
        for word in words(tweet):
            count[word] += 1
            total += 1

    for word in count.keys():
        print "%s %f" % (word.encode('utf-8') , float(count[word])/total)

if __name__ == '__main__':
    main()
