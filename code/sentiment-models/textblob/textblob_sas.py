from textblob import TextBlob
import nltk
import pandas as pd



def textblob_sentiment(path,k):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        score = each.sentiment[0]
        if score < 0:
            sentiment.append(0)
        else:
            sentiment.append(1)



    text = []
    for each in set['Sentences']:
        text.append(each)

    g1 = {'Gender':set['Gender'],'Emotion':set['Emotion'],'Sentiment':sentiment}

    if k == 2:
        g2 = {'Gender':set['Gender'],'Race':set['Race'],'Emotion':set['Emotion'],'Sentiment':sentiment}
        return g2
    elif k == 1:
        return g1



def g1(path,i,k):

    df = textblob_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group1/textblob/e{}_tb.csv'.format(i),index=False)

def g2(path,k):

    df = textblob_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group2/textblob/e3_tb.csv',index=False)



def g3(path,i,k):

    df = textblob_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group3/textblob/e{}_tb.csv'.format(i),index=False)

def g4(path,k):

    df = textblob_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group4/textblob/e3_tb.csv',index=False)
