from typing import Optional

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

score_threshold = 0.5


def vader_extract_sentiment(to_be_computed: str, sentiment_counter: [],
                            expected_sentiment: str) -> Optional[int]:
    compound_score = analyzer.polarity_scores(to_be_computed)['compound']
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
    if computed_sentiment == "negative":
        sentiment_counter[1] += 1
    if computed_sentiment == "neutral":
        sentiment_counter[2] += 1

    if computed_sentiment == expected_sentiment:
        return 1
    return 0
