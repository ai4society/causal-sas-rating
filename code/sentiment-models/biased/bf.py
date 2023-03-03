import pandas as pd



def bf_sentiment(path,k,c):

    set = pd.read_csv(path,engine="python")

    senti = []
    if c == 0:
        for (text,gender) in zip(set['Sentences'],set['Gender']):
            if gender==2:
                senti.append(1)
            else:
                senti.append(0)
    else:
        for (text,gender) in zip(set['Sentences'],set['Gender']):
            if gender==2:
                senti.append(1)
            else:
                senti.append(-1)

    text = []
    for each in set['Sentences']:
        text.append(each)

    g1 = {'Gender':set['Gender'],'Emotion':set['Emotion'],'Sentiment':senti}

    if k == 2:
        g2 = {'Gender':set['Gender'],'Race':set['Race'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g2
    elif k == 1:
        return g1

def bf_allure(path):

    set = pd.read_csv(path,engine="python")

    senti = []
    for (text,gender) in zip(set['Text'],set['User_gender']):
        if gender==2:
            senti.append(1)
        else:
            senti.append(-1)

    g = {'C_num': set['C_num'], 'UB': set['UB'], 'User_gender':set['User_gender'], 'Text':set['Text'], 'Sentiment': senti}

    return g


def g1(path,i,k,c):

    df = bf_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group1/biased/e{}_bf.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group1/biased/e{}_bf.csv'.format(i),index=False)


def g2(path,i,k,c):

    df = bf_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group2/biased/e{}_bf.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group2/biased/e{}_bf.csv'.format(i),index=False)

def g3(path,i,k,c):

    df = bf_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group3/biased/e{}_bf.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group3/biased/e{}_bf.csv'.format(i),index=False)

def g4(path,i,k,c):

    df = bf_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group4/biased/e{}_bf.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group4/biased/e{}_bf.csv'.format(i),index=False)

def allure_data(path):

    df = bf_allure(path)
    final_df = pd.DataFrame(df)
    final_df.to_csv('../data/results/real-world/allure/bf/bf.csv',index=False)
