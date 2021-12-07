import argparse

import pandas as pd

from sentiment_finder import extract_sentiment

p = argparse.ArgumentParser()
p.add_argument("-dataset_src", type=str, help="the source directory containing all the imdb statement files")


def execute_twitter_dataset(base_path: str):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    dataframe = pd.read_csv(base_path)
    for index, row in dataframe.iterrows():
        hits += extract_sentiment(row['text'], 0.5, pos_neg_neu, row['airline_sentiment'])
        analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")


execute_twitter_dataset(p.parse_args().dataset_src)
