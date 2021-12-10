from typing import Optional

from textblob import TextBlob

score_threshold = 0.05


def textblob_extract_sentiment(to_be_computed: str, sentiment_counter: [],
                               expected_sentiment: str) -> Optional[int]:
    blob = TextBlob(to_be_computed)
    compound_score = blob.sentiment.polarity
    if compound_score < -score_threshold:
        computed_sentiment = "negative"
    elif compound_score > score_threshold:
        computed_sentiment = "positive"
    elif -score_threshold <= compound_score <= score_threshold:
        computed_sentiment = "neutral"
    else:
        return None

    if computed_sentiment == "positive":
        sentiment_counter[0] += 1
        # print(f"{to_be_computed} -> positive")
    if computed_sentiment == "negative":
        sentiment_counter[1] += 1
        # print(f"{to_be_computed} -> negative")
    if computed_sentiment == "neutral":
        sentiment_counter[2] += 1
        # print(f"{to_be_computed} -> neutral")

    if computed_sentiment == expected_sentiment:
        return 1
    return 0
