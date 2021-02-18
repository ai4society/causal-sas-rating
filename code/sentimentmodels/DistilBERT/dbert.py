import pandas as pd
from transformers import pipeline
sentimentanalyzer = pipeline("sentiment-analysis")

# result = sentimentanalyzer("I really don't like what you did")[0]
# print(f"Sentiment: {result}")
#
# result = sentimentanalyzer("I really like what you did")[0]
# print(f"Sentiment: {result}")
#
# result = sentimentanalyzer("This is good")[0]
# print(f"Sentiment: {result}")


def bertsentiment(path,file_name):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        sen_temp = sentimentanalyzer(each)[0]
        if sen_temp['label'] == 'POSITIVE':
            senti.append(sen_temp['score'])
        elif sen_temp['label'] == 'NEGATIVE':
            senti.append(0 - sen_temp['score'])
        else:
            senti.append(sen_temp['score'])

    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':senti}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])

    final_df.to_csv('../../data/results/distilbert/nonames/{}.csv'.format(file_name))


def bertsentiment_name(path,file_name):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        sen_temp = sentimentanalyzer(each)[0]
        if sen_temp['label'] == 'POSITIVE':
            senti.append(sen_temp['score'])
        elif sen_temp['label'] == 'NEGATIVE':
            senti.append(0 - sen_temp['score'])
        else:
            senti.append(sen_temp['score'])

    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':senti}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])

    final_df.to_csv('../../data/results/distilbert/withnames/{}.csv'.format(file_name))
