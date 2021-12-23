import pandas as pd


def get_expected_sentiment_from_row(row):
    expected_sentiment = "negative" if row[0] == 0 else None
    expected_sentiment = "neutral" if row[0] == 2 else None
    expected_sentiment = "positive" if row[0] == 4 else None
    return expected_sentiment


def sentiment140_reader_execute(base_path: str, sentiment_core_matcher):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    dataframe = pd.read_csv(base_path, encoding="latin-1")
    for index, row in dataframe.iterrows():
        hits += sentiment_core_matcher(row[5], pos_neg_neu, get_expected_sentiment_from_row(row))
        analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
        print(f"accuracy % {(hits / analyzed_rows) * 100} ")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")
