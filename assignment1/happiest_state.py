import sys
import operator
import json
from collections import defaultdict

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
'VA': 'Virginia',
'VI': 'Virgin Islands',
'VT': 'Vermont',
'WA': 'Washington',
'WI': 'Wisconsin',
'WV': 'West Virginia',
'WY': 'Wyoming'
}


def create_sentiment_dict(afinnfile):
    afinnfile = open(afinnfile)
    scores = {}
    for line in afinnfile:
        term, score  = line.split("\t")
        scores[term] = int(score)
    return scores


def words(tweet):
    return tweet["text"].split()


def sentiment(tweet, scores):
    score = sum(map(lambda w: scores.get(w, 0), words(tweet)))
    return score


def is_valid(tweet):
    return "text" in tweet.keys() and \
            tweet["lang"] == "en" and \
            tweet["place"] and \
            tweet["place"]["country_code"].upper() == "US"


def tweets(filename):
    tweets  = map(json.loads, open(filename).readlines())
    return filter(is_valid, tweets)


def state_abbr(tweet):
    return tweet["place"]["full_name"].split(",")[-1].strip()


def main():
    sent_filename = sys.argv[1]
    tweet_filename = sys.argv[2]

    scores = create_sentiment_dict(sent_filename)
    state_sentiment = defaultdict(int)

    for tweet in tweets(tweet_filename):
        abbr = state_abbr(tweet)
        if abbr in states.keys():
            state_sentiment[abbr] += sentiment(tweet, scores)

    state_sentiment_sorted = sorted(state_sentiment.iteritems(), key=operator.itemgetter(1), reverse=True)
    happiest = state_sentiment_sorted[0][0]

    #for item in state_sentiment_sorted:
        #print "%s %i" % item

    print happiest

if __name__ == '__main__':
    main()

