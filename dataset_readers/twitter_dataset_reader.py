import pandas as pd


def twitter_reader_execute(base_path: str, sentiment_core_matcher):
    pd.set_option("display.max_columns", None)
    pd.set_option("display.max_rows", None)

    pos_neg_neu = [0, 0, 0]
    hits, analyzed_rows = 0, 0
    dataframe = pd.read_csv(base_path)
    for index, row in dataframe.iterrows():
        hits += sentiment_core_matcher(row['text'], pos_neg_neu, row['airline_sentiment'])
        analyzed_rows += 1
        print(f"positives {pos_neg_neu[0]} ### negatives {pos_neg_neu[1]} ### neutrals {pos_neg_neu[2]}")
        print(f"accuracy % {(hits / analyzed_rows) * 100} ")
    print(f"hits: {hits}, analyzed rows: {analyzed_rows}")
