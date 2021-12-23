from typing import Optional

import boto3


def awscomprehend_extract_sentiment(to_be_computed: str, sentiment_counter: [],
                                    expected_sentiment: str) -> Optional[int]:
    client = boto3.client("comprehend", region_name="us-east-2")
    resp = client.detect_sentiment(Text=to_be_computed, LanguageCode="en")
    computed_sentiment = resp["Sentiment"].lower()

    if computed_sentiment == "positive":
        sentiment_counter[0] += 1
    if computed_sentiment == "negative":
        sentiment_counter[1] += 1
    if computed_sentiment == "neutral":
        sentiment_counter[2] += 1

    if computed_sentiment == expected_sentiment:
        return 1
    return 0
