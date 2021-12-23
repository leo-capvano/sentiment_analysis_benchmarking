import os
from typing import Optional

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

key = str(os.environ.get("AZURE_KEY"))
credential = AzureKeyCredential("")  # TODO remove
text_analytics_client = TextAnalyticsClient(
    endpoint="https://text-language-engine-resource.cognitiveservices.azure.com/",
    credential=credential)


def azure_extract_sentiment(to_be_computed: str, sentiment_counter: [],
                            expected_sentiment: str) -> Optional[int]:
    computed_sentiment = text_analytics_client.analyze_sentiment([to_be_computed], language="en")[0].sentiment
    if computed_sentiment == "positive":
        sentiment_counter[0] += 1
    if computed_sentiment == "negative":
        sentiment_counter[1] += 1
    if computed_sentiment == "neutral":
        sentiment_counter[2] += 1

    if computed_sentiment == expected_sentiment:
        return 1
    return 0
