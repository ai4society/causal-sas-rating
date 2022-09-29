import pandas as pd



def bf_sentiment(path,k):

    set = pd.read_csv(path,engine="python")

    senti = []
    for (text,gender) in zip(set['Sentences'],set['Gender']):
        if gender==2:
            senti.append(1)
        else:
            senti.append(0)

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

    df = bf_sentiment(path)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group1/biased/e{}_bf.csv'.format(i),index=False)

def g2(path,k):

    df = bf_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group2/biased/e3_bf.csv',index=False)

def g3(path,i,k):

    df = bf_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group3/biased/e{}_bf.csv'.format(i),index=False)

def g4(path,k):

    df = bf_sentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    final_df.to_csv('../data/results/group4/biased/e3_bf.csv',index=False)
