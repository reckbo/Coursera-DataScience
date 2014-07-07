import sys
import json
import operator
from pprint import pprint
from collections import defaultdict


def is_valid(tweet):
    return "entities" in tweet.keys()


def tweets(filename):
    tweets  = map(json.loads, open(filename).readlines())
    return filter(is_valid, tweets)


def hashtags(tweet):
    return map(lambda x: x.get("text"), tweet["entities"]["hashtags"])


def main():
    tweet_filename = sys.argv[1]

    hashtag_count = defaultdict(int)

    for tweet in tweets(tweet_filename):
        for hashtag in hashtags(tweet):
            hashtag_count[hashtag] += 1

    sorted_hashtags = sorted(hashtag_count.iteritems(), key=operator.itemgetter(1), reverse=True)

    for hashtag in sorted_hashtags[:10]:
        print "%s %i" % hashtag

if __name__ == '__main__':
    main()

