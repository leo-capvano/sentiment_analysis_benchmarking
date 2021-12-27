import os
from typing import Optional

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from dataset_readers.imdb_dataset_reader import imdb_reader_execute

key = str(os.environ.get("AZURE_KEY"))
credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(
    endpoint="https://text-language-engine-resource.cognitiveservices.azure.com/",
    credential=credential)


def azure_extract_sentiment(to_be_computed: str, sentiment_counter: [],
                            expected_sentiment: str) -> Optional[int]:
    analysis_response = text_analytics_client.analyze_sentiment([to_be_computed], language="en")[0]
    computed_sentiment = analysis_response.sentiment
    if computed_sentiment == "mixed":
        computed_confidence_scores = [analysis_response.confidence_scores.positive,
                                      analysis_response.confidence_scores.negative,
                                      analysis_response.confidence_scores.neutral]
        computed_sentiment_index = computed_confidence_scores.index(max(computed_confidence_scores))
        if computed_sentiment_index == 0:
            computed_sentiment = "positive"
        elif computed_sentiment_index == 1:
            computed_sentiment = "negative"
        elif computed_sentiment_index == 2:
            computed_sentiment = "neutral"
    if computed_sentiment == "positive":
        sentiment_counter[0] += 1
    if computed_sentiment == "negative":
        sentiment_counter[1] += 1
    if computed_sentiment == "neutral":
        sentiment_counter[2] += 1

    if computed_sentiment == expected_sentiment:
        return 1
    return 0


if __name__ == '__main__':
    imdb_reader_execute("..\\resources\\imdb_dataset.csv", azure_extract_sentiment)
