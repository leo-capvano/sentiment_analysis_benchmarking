import pandas as pd


def imdb_reader_execute(base_path: str, sentiment_core_matcher):
    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    dataframe = pd.read_csv(base_path, encoding="latin-1")
    for index, row in dataframe.iterrows():
        if len(row[0]) < 5000:
            try:
                hits += sentiment_core_matcher(row[0], pos_neg_neu, row[1])
            except Exception as e:
                print(e)
                continue
            analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
        print(f"accuracy % {(hits / analyzed_rows) * 100} ")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")
