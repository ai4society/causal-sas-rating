import pandas as pd
from transformers import pipeline
sentimentanalyzer = pipeline("sentiment-analysis")

def bertsentiment(path,k,c):

    set = pd.read_csv(path,engine="python")
    senti = []
    for each in set['Sentences']:
        sen_temp = sentimentanalyzer(each)[0]
        if sen_temp['label'] == 'POSITIVE':
            senti.append(1)
        elif sen_temp['label'] == 'NEGATIVE':
            senti.append(0)
        else:
            senti.append(1)

    text = []
    for each in set['Sentences']:
        text.append(each)


    if k == 2:
        g2 = {'Gender':set['Gender'],'Race':set['Race'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g2
    elif k == 1:
        g1 = {'Gender':set['Gender'],'Emotion':set['Emotion'],'Sentiment':senti}
        return g1

def dbert_allure(path):

    set = pd.read_csv(path,engine="python")
    senti = []
    for each in set['Text']:
        sen_temp = sentimentanalyzer(each)[0]
        if sen_temp['label'] == 'POSITIVE':
            senti.append(1)
        elif sen_temp['label'] == 'NEGATIVE':
            senti.append(0)
        else:
            senti.append(1)



    g = {'C_num': set['C_num'], 'UB': set['UB'], 'User_gender':set['User_gender'], 'Text':set['Text'], 'Sentiment': senti}
    
    return g
    

def g1(path,i,k,c):

    df = bertsentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group1/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group1/dbert/e{}_dbert.csv'.format(i),index=False)

def g2(path,i,k,c):

    df = bertsentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group2/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group2/dbert/e{}_dbert.csv'.format(i),index=False)

def g3(path,i,k,c):

    df = bertsentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group3/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group3/dbert/e{}_dbert.csv'.format(i),index=False)

def g4(path,i,k,c):

    df = bertsentiment(path,k)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group4/dbert/e{}_dbert.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group4/dbert/e{}_dbert.csv'.format(i),index=False)

def allure_data(path):
    
    df = dbert_allure(path)
    final_df = pd.DataFrame(df)
    final_df.to_csv('../data/results/real-world/allure/dbert/dbert.csv',index=False)