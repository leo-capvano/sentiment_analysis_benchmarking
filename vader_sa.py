from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

sentences = [
    "Once again Mr. Costner has dragged out a movie for far longer than necessary. Aside from the terrific sea rescue "
    "sequences, of which there are very few I just did not care about any of the characters. Most of us have ghosts "
    "in the closet, and Costner's character are realized early on, and then forgotten until much later, by which time "
    "I did not care. The character we should really care about is a very cocky, overconfident Ashton Kutcher. The "
    "problem is he comes off as kid who thinks he's better than anyone else around him and shows no signs of a "
    "cluttered closet. His only obstacle appears to be winning over Costner. Finally when we are well past the half "
    "way point of this stinker, Costner tells us all about Kutcher's ghosts. We are told why Kutcher is driven to be "
    "the best with no prior inkling or foreshadowing. No magic here, it was all I could do to keep from turning it "
    "off an hour in."]

if __name__ == '__main__':
    analyzer = SentimentIntensityAnalyzer()
    for sentence in sentences:
        vs = analyzer.polarity_scores(sentence)
        print(sentence + " -> " + str(vs))
