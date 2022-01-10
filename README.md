# Sentiment analysis tools benchmarking

## Description

```
 The sentiment analysis is the use of natural language processing, text analysis, 
 computational linguistics, and biometrics to systematically identify, extract,
 quantify, and study affective states and subjective information.
 
 The aim of this project is to measure the accuracy of the most popular sentiment analysis tools.
```

The benchmark test was carried out by using the below described datasets:

- IMDb Dataset: containing a list of movie review divided into negative and positive statements. It contains the most
  25k popular reviews. [source](http://ai.stanford.edu/~amaas/data/sentiment/)
- Twitter US Airlines Dataset: containing the tweets about each of the major US airlines since Feb 2015. Each tweet il
  classified positive, negative or
  neutral. [source](https://www.kaggle.com/crowdflower/twitter-airline-sentiment/version/4)
- Sentiment140 dataset: this dataset contains various tweets record that includes polarity, date, and the tweet
  text [source](http://help.sentiment140.com/for-students)

The minimum information contained by each record of those datasets are:

- the text to analyze
- the related correct sentiment

## Overview:

The project has one entrypoint file: **make_benchmark.py**. It has dedicated commands to execute a benchmark with a
specific dataset and a specific sentiment analysis tool. The entrypoint will then call two of the underlying layers:

1. **dataset reader**: a module that reads the dataset and pre-process/standardizes the data to adapt them to the
   sentiment analysis core procedure
2. **sentiment matcher**: is the sentiment analysis core procedure which acts as result post-process; it understands the
   results and standardizes them to the caller in order to calculate the sentiment hit or sentiment miss. Each sentiment
   matcher knows the correct sentiment for each record; this allows to calculate a sentiment hit or sentiment miss.

### Commands

**-dataset**: allow you to select one of the supported dataset to execute the benchmark. The possibile values are:

- _-imdb_: to select the imdb dataset
- _-twitter_: to select the twitter dataset
- _-sentiment140_: to select the sentiment140 dataset

**-tool**: allow you to specify the tool to use to execute the sentiment analysis prediction/benchmark

- _-vader_: to select vader as sentiment analysis executor tool
- _-textblob_: to select textblob as sentiment analysis executor tool
- _-azure_: to select azure text-language-engine as sentiment analysis executor tool
- _-aws_: to select amazon comprehend as sentiment analysis executor tool

An example of execution with azure text-language-engine as sentiment analysis engine and the sentiment140 dataset as
input of the benchmark:

```
python make_benchmark.py -dataset sentiment140_dataset.csv -tool azure
```

An example of response that shows the number of sentiment hit and sentiment miss:

```
.
...
.....
positives 739 ### negatives 574 ### neutrals 1039
positives 739 ### negatives 574 ### neutrals 1040
positives 739 ### negatives 574 ### neutrals 1041
positives 739 ### negatives 574 ### neutrals 1041
hits: 523, analyzed rows: 2470
```

# Usage Examples
To run a benchmark of the **vader** tool given **imdb sentences dataset** as input:
```
python .\make_benchmark.py -dataset imdb -tool vader
```
To run a benchmark of the **textblob** tool given **imdb sentences dataset** as input:
```
python .\make_benchmark.py -dataset imdb -tool textblob
```
To run a benchmark of the **textblob** tool given **sentiment140 dataset** as input:
```
python .\make_benchmark.py -dataset sentiment140 -tool textblob
```
To run a benchmark of the **aws** tool given **sentiment140 dataset** as input:
```
python .\make_benchmark.py -dataset sentiment140 -tool aws
```
To run a benchmark of the **azure** tool given **twitter dataset** as input:
```
python .\make_benchmark.py -dataset twitter -tool azure
```

## How to configure credential for AWS and Azure services
### AWS
1. Create _.aws_ folder under C:/Users/_user_/
2. Create the file .aws/credentials
3. The credentials file will contain:
```
[default]
aws_access_key_id = ...
aws_secret_access_key = ...
```
4. the AWS comprehend client automatically reads the credentials file to open the connection

### Azure
The azure_sentiment_matcher.py module reads the Azure endpoint key from an environment
variable called _AZURE_KEY_, so:
1. Get the endpoint key from the Azure resource manager portal
2. Create the _AZURE_KEY_ environment variable and assign it the key value
3. You are ready to run the azure_sentiment_matcher.py


