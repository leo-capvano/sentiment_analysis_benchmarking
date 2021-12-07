import argparse
import os

from sentiment_finder import extract_sentiment

p = argparse.ArgumentParser()
p.add_argument("-dataset_src", type=str, help="the source directory containing all the imdb statement files")
p.add_argument("-expected_sentiment", type=str, help="the expected sentiment")


def execute_imdb_dataset(base_path: str, expected_sentiment: str):
    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    for filename in os.listdir(base_path):
        with open(os.path.join(base_path, filename), "r", encoding="utf-8") as file:
            hits += extract_sentiment(file.read(), 0.5, pos_neg_neu, expected_sentiment)
            analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
    return hits, analyzed_rows


sentiment_hits, total_rows = execute_imdb_dataset(p.parse_args().dataset_src, p.parse_args().expected_sentiment)

print(f"hits: {sentiment_hits}, analyzed rows: {total_rows}")
