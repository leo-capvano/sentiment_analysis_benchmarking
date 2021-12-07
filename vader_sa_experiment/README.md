# Description
In this section you can find the usage explanation for each of the dataset execution. 
Each different script file represents a data preparation step (for each different dataset) before executing the core sentiment analysis procedure
(that is the **sentiment_finder.py** module). In the following doc it's described how to run a sentiment analysis benchmark test
for each of the supported dataset.

## IMDb dataset execution

```
An example of execution:
python .\imdb_dataset_sa.py 
    -dataset_src C:\Users\user\sentiment_example\resources\imdb_dataset\test\pos 
    -expected_sentiment positive
```

- -dataset_src indicates the path pointing to the directory that contains positive or negative files
- -expected_sentiment is the sentiment that we expect

in the example we are executing sentiment analysis benchmarking on the **..\\pos** folder, and we expect that every
statement belonging to that folder will be classified as **positive**

The output of the above execution shows the cumulative count for each classification, the number of hits and the total
number of analyzed rows:

```
.
..
...
positives 4916 ### negatives 5684 ### neutrals 1897
positives 4917 ### negatives 5684 ### neutrals 1897
positives 4918 ### negatives 5684 ### neutrals 1897
positives 4919 ### negatives 5684 ### neutrals 1897
hits: 5684, analyzed rows: 12500
```

## Twitter dataset execution

```
An example of execution:
python .\twitter_dataset_sa.py 
    -dataset_src C:\Users\user\sentiment_example\resources\dataset_tweets_us_airlines.csv.csv
```

- -dataset_src indicates the path pointing to the directory that contains positive or negative files

In this example we are executing sentiment analysis benchmarking on the **..\\dataset_tweets_us_airlines.csv** file;
since each record contains the correct sentiment, the script automatically counts the number of sentiment hits and
sentiment miss.

The output of the above execution, as above, shows the cumulative count for each classification, the number of hits and
the total number of analyzed rows:

```
.
..
...
positives 4916 ### negatives 5684 ### neutrals 1897
positives 4917 ### negatives 5684 ### neutrals 1897
positives 4918 ### negatives 5684 ### neutrals 1897
positives 4919 ### negatives 5684 ### neutrals 1897
hits: 5684, analyzed rows: 12500
```

## Sentiment140 dataset execution

```
**An example of execution:**
python .\sentiment140_dataset_sa.py 
    -dataset_src C:\Users\user\sentiment_example\resources\sentiment140_dataset.csv
```

- -dataset_src indicates the path pointing to the directory that contains positive or negative files

In this example we are executing sentiment analysis benchmarking on the **..\\sentiment140_dataset.csv** file;
since each record contains the correct sentiment, the script automatically counts the number of sentiment hits and
sentiment miss.

The output of the above execution, as above, shows the cumulative count for each classification, the number of hits and
the total number of analyzed rows:

```
.
..
...
positives 4916 ### negatives 5684 ### neutrals 1897
positives 4917 ### negatives 5684 ### neutrals 1897
positives 4918 ### negatives 5684 ### neutrals 1897
positives 4919 ### negatives 5684 ### neutrals 1897
hits: 5684, analyzed rows: 12500
```