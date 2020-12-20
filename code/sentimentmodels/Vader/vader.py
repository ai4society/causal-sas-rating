import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#Function to calculate sentiment scores.
def sentiment_rating(sentence):
    #Creating sentiment analyzer object.
    senti = SentimentIntensityAnalyzer()
    #SentimentIntensityAnalyzer() gives a dictionary which has pos,neg,neutral and compound scores.
    senti_dict = senti.polarity_scores(sentence)

    return senti_dict

def vadersentiment(path,file_name):
    #Loading the dataset
    set = pd.read_csv(path,engine="python")
    #Seperating sentence,race and gender into lists.
    eec = []
    for each in set['Sentences']:
        eec.append(each)

    sentiment = []
    for each in eec:
        sentiment.append(sentiment_rating(each)['compound'])

    d = {'Sentences':eec,'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentences','Gender','Sentiment'])

    final_df.to_csv('../../data/results/vader/{}.csv'.format(file_name))
