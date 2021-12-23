import pandas as pd


def imdb_reader_execute(base_path: str, sentiment_core_matcher):
    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    dataframe = pd.read_csv(base_path, encoding="latin-1")
    for index, row in dataframe.iterrows():
        if len(row[0]) < 5000:
            hits += sentiment_core_matcher(row[0], pos_neg_neu, row[1])
            analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
        print(f"accuracy % {(hits / analyzed_rows) * 100} ")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")

# if __name__ == '__main__':
#     base_path = "..\\resources\\imdb_dataset.csv"
#     imdb_reader_execute(base_path, textblob_extract_sentiment)
