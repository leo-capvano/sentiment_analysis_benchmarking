import os

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def extract_sentiment(to_be_computed: str, score_threshold: float, sentiment_counter: [], expected_sentiment: str):
    compound_score = analyzer.polarity_scores(to_be_computed)['compound']
    if compound_score < -score_threshold:
        computed_sentiment = "negative"
    elif compound_score > score_threshold:
        computed_sentiment = "positive"
    elif -score_threshold <= compound_score <= score_threshold:
        computed_sentiment = "neutral"
    else:
        return

    if computed_sentiment == "positive":
        sentiment_counter[0] += 1
        print(f"{to_be_computed} -> positive")
    if computed_sentiment == "negative":
        sentiment_counter[1] += 1
        print(f"{to_be_computed} -> negative")
    if computed_sentiment == "neutral":
        sentiment_counter[2] += 1
        print(f"{to_be_computed} -> neutral")

    if computed_sentiment == expected_sentiment:
        return 1
    return 0


def execute_twitter_dataset():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    dataframe = pd.read_csv("C:\\Users\\leoca\\Desktop\\datasets_sa\\dataset_tweets_us_airlines.csv.csv")
    for index, row in dataframe.iterrows():
        hits += extract_sentiment(row['text'], 0.5, pos_neg_neu, row['airline_sentiment'])
        analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")


def execute_imdb_dataset(base_path: str, expected_sentiment: str):
    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    for filename in os.listdir(base_path):
        with open(os.path.join(base_path, filename), "r", encoding="utf-8") as file:
            hits += extract_sentiment(file.read(), 0.5, pos_neg_neu, expected_sentiment)
            analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")


if __name__ == '__main__':
    execute_twitter_dataset()
    # execute_imdb_dataset("C:\\Users\\leoca\\Desktop\\datasets_sa\\imdb_dataset\\test\\neg", "negative")
    # execute_imdb_dataset("C:\\Users\\leoca\\Desktop\\datasets_sa\\imdb_dataset\\test\\pos", "positive")
