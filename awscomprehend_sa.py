import boto3

if __name__ == '__main__':
    client = boto3.client("comprehend", region_name = "us-east-2")
    sentiment = client.detect_sentiment(Text = "ciao sono leo", LanguageCode = "it")
    print(sentiment)