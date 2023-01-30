import pandas as pd
import random



def gen_random():
    num = random.random()

    if random.random() < 0.5:
        return 1
    else:
        return 0


def random_sentiment(path,k):

    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(gen_random())

    text = []
    for each in set['Sentences']:
        text.append(each)

    g1 = {'Gender':set['Gender'],'Emotion':set['Emotion'],'Sentiment':senti}


    if k == 2:
        g2 = {'Gender':set['Gender'],'Race':set['Race'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g2
    elif k == 1:
        return g1


def g1(path,i,k):

    df = random_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group1/random/e{}_random.csv'.format(i),index=False)

def g2(path,i,k):

    df = random_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group2/random/e{}_random.csv'.format(i),index=False)


def g3(path,i,k):

    df = random_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group3/random/e{}_random.csv'.format(i),index=False)

def g4(path,i,k):

    df = random_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group4/random/e{}_random.csv'.format(i),index=False)
