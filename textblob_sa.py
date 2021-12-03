from textblob import TextBlob

if __name__ == '__main__':
    text = TextBlob("Ipad is a great tool")
    print(text.sentiment)
    print(text.tags)
