import pandas as pd
import random
import numpy as np


def gen_random():
    num = random.random()

    if random.random() < 0.5:
        return 1
    else:
        return 0

def gen_random_cont():

    num = round(np.random.uniform(-1,1),2)

    return num


def random_sentiment(path,k,c):

    set = pd.read_csv(path,engine="python")

    senti = []

    if c == 0:
        for each in set['Sentences']:
            senti.append(gen_random())
    else:
        for each in set['Sentences']:
            senti.append(gen_random_cont())

    text = []
    for each in set['Sentences']:
        text.append(each)

    g1 = {'Gender':set['Gender'],'Emotion':set['Emotion'],'Sentiment':senti}


    if k == 2:
        g2 = {'Gender':set['Gender'],'Race':set['Race'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g2
    elif k == 1:
        return g1


def g1(path,i,k,c):

    df = random_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group1/random/e{}_random.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group1/random/e{}_random.csv'.format(i),index=False)

def g2(path,i,k,c):

    df = random_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group2/random/e{}_random.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group2/random/e{}_random.csv'.format(i),index=False)

def g3(path,i,k,c):

    df = random_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group3/random/e{}_random.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group3/random/e{}_random.csv'.format(i),index=False)

def g4(path,i,k,c):

    df = random_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group4/random/e{}_random.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group4/random/e{}_random.csv'.format(i),index=False)
