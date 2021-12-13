import argparse

from dataset_readers.imdb_dataset_reader import imdb_reader_execute
from dataset_readers.sentiment140_dataset_reader import sentiment140_reader_execute
from dataset_readers.twitter_dataset_reader import twitter_reader_execute
from sentiment_matchers.awscomprehend_sentiment_matcher import awscomprehend_extract_sentiment
from sentiment_matchers.azure_sentiment_matcher import azure_extract_sentiment
from sentiment_matchers.textblob_sentiment_matcher import textblob_extract_sentiment
from sentiment_matchers.vader_sentiment_matcher import vader_extract_sentiment

IMDB_POSITIVE_DATASET_PATH = "resources\\imdb_dataset\\test\\pos"

IMDB_NEGATIVE_DATASET_PATH = "resources\\imdb_dataset\\test\\neg"

TWITTER_DATASET_PATH = "resources\\tweeter_dataset.csv"

SENTIMENT140_DATASET_PATH = "resources\\sentiment140_dataset.csv"

p = argparse.ArgumentParser()
p.add_argument("-expected_sentiment", type=str, help="the expected sentiment")
p.add_argument("-dataset", type=str, help="the dataset reader to use",
               choices=["imdb-pos", "imdb-neg", "twitter", "sentiment140"])
p.add_argument("-tool", type=str, help="the sentiment analysis to use", choices=["vader", "textblob", "aws", "azure"])

args = p.parse_args()


def get_sentiment_matcher(tool):
    if tool == "vader":
        return vader_extract_sentiment
    elif tool == "textblob":
        return textblob_extract_sentiment
    elif tool == "aws":
        return awscomprehend_extract_sentiment
    elif tool == "azure":
        return azure_extract_sentiment
    else:
        print("the selected tool is not supported")
        exit(0)


if args.dataset == "imdb-pos":
    imdb_reader_execute(IMDB_POSITIVE_DATASET_PATH, args.expected_sentiment, get_sentiment_matcher(args.tool))
elif args.dataset == "imdb-neg":
    imdb_reader_execute(IMDB_NEGATIVE_DATASET_PATH, args.expected_sentiment, get_sentiment_matcher(args.tool))
elif args.dataset == "twitter":
    twitter_reader_execute(TWITTER_DATASET_PATH, get_sentiment_matcher(args.tool))
elif args.dataset == "sentiment140":
    sentiment140_reader_execute(SENTIMENT140_DATASET_PATH, get_sentiment_matcher(args.tool))
else:
    print("the selected dataset is not supported")
    exit(0)
