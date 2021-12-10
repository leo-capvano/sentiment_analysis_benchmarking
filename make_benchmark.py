import argparse

from dataset_readers.imdb_dataset_reader import imdb_reader_execute
from dataset_readers.sentiment140_dataset_reader import sentiment140_reader_execute
from dataset_readers.twitter_dataset_reader import twitter_reader_execute
from sentiment_matchers.awscomprehend_sentiment_matcher import awscomprehend_extract_sentiment
from sentiment_matchers.textblob_sentiment_matcher import textblob_extract_sentiment
from sentiment_matchers.vader_sentiment_matcher import vader_extract_sentiment

p = argparse.ArgumentParser()
p.add_argument("-dataset_src", type=str, help="the source directory containing all the imdb statement files")
p.add_argument("-expected_sentiment", type=str, help="the expected sentiment")
p.add_argument("-dataset", type=str, help="the dataset reader to use", choices=["imdb", "twitter", "sentiment140"])
p.add_argument("-tool", type=str, help="the sentiment analysis to use", choices=["vader", "textblob", "aws"])

args = p.parse_args()


def get_sentiment_matcher(tool):
    if tool == "vader":
        return vader_extract_sentiment
    elif tool == "textblob":
        return textblob_extract_sentiment
    elif tool == "aws":
        return awscomprehend_extract_sentiment


if args.dataset == "imdb":
    imdb_reader_execute(args.dataset_src, args.expected_sentiment, get_sentiment_matcher(args.tool))
elif args.dataset == "twitter":
    twitter_reader_execute(args.dataset_src, get_sentiment_matcher(args.tool))
elif args.dataset == "sentiment140":
    sentiment140_reader_execute(args.dataset_src, get_sentiment_matcher(args.tool))
else:
    exit(0)
