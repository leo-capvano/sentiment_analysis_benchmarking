import os


def imdb_reader_execute(base_path: str, expected_sentiment: str, sentiment_core_matcher):
    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    for filename in os.listdir(base_path):
        with open(os.path.join(base_path, filename), "r", encoding="utf-8") as file:
            hits += sentiment_core_matcher(file.read(), 0.5, pos_neg_neu, expected_sentiment)
            analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
    return hits, analyzed_rows
