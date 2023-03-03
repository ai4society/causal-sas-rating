import pandas as pd
from transformers import pipeline
sentimentanalyzer = pipeline("sentiment-analysis")

def bertsentiment(path,k,c):

    set = pd.read_csv(path,engine="python")
    senti = []

    if c == 0:
        for each in set['Sentences']:
            sen_temp = sentimentanalyzer(each)[0]
            if sen_temp['label'] == 'POSITIVE':
                senti.append(1)
            elif sen_temp['label'] == 'NEGATIVE':
                senti.append(0)
            else:
                senti.append(1)
    else:
        for each in set['Sentences']:
            sen_temp = sentimentanalyzer(each)[0]
            if sen_temp['label'] == 'POSITIVE':
                senti.append(round(sen_temp['score'],2))
            elif sen_temp['label'] == 'NEGATIVE':
                senti.append(round((0 - sen_temp['score']),2))
            else:
                senti.append(round(sen_temp['score'],2))

    text = []
    for each in set['Sentences']:
        text.append(each)


    if k == 2:
        g2 = {'Gender':set['Gender'],'Race':set['Race'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g2
    elif k == 1:
        g1 = {'Gender':set['Gender'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g1


def g1(path,i,k,c):

    df = bertsentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group1/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group1/dbert/e{}_dbert.csv'.format(i),index=False)

def g2(path,i,k,c):

    df = bertsentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group2/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group2/dbert/e{}_dbert.csv'.format(i),index=False)

def g3(path,i,k,c):

    df = bertsentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group3/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group3/dbert/e{}_dbert.csv'.format(i),index=False)

def g4(path,i,k,c):

    df = bertsentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group4/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group4/dbert/e{}_dbert.csv'.format(i),index=False)
