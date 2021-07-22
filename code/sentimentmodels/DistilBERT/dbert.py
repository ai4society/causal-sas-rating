import pandas as pd
from transformers import pipeline
sentimentanalyzer = pipeline("sentiment-analysis")




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

def bertsentiment_baseline(path):
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

    set['Sentiment_dbert'] = senti
    set.to_csv(path,index=False)


def bertsentiment_sentence_baseline(path,token):
    original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

    template = sorted(set(original_data['Template']))
    template = list([template[0],template[4],template[6],template[10]])

    male = list(sorted(set(original_data[original_data['Gender']=='male']['Person'])))[-10:]
    male[0] = male[0].replace("him","my nephew")

    female = list(sorted(set(original_data[original_data['Gender']=='female']['Person'])))[-10:]
    female[7] = female[7].replace("she","my niece")

    emo = list(set(original_data["Emotion word"]))
    emo = [each for each in emo if str(each) != 'nan']
    emo = sorted(emo)

    emotion_words = [emo[21],emo[22],emo[4],emo[30],emo[6],emo[16],emo[3],emo[18],emo[28],emo[12]]

    dataset = pd.read_csv(path,engine="python")
    words = []
    male_sentiment = []
    for each in dataset['male sentences']:
        sen_temp = sentimentanalyzer(each)[0]
        if sen_temp['label'] == 'POSITIVE':
            male_sentiment.append(sen_temp['score'])
        elif sen_temp['label'] == 'NEGATIVE':
            male_sentiment.append(0 - sen_temp['score'])
        else:
            male_sentiment.append(sen_temp['score'])

    k = 0
    male_averages = []
    for m in range(40):
        total = 0
        for each in male_sentiment[k:k+10]:
            total = total + each
        average = total / 10
        male_averages.append(round(average,2))
        k = k+10
    print(len(male_averages))

    female_sentiment = []
    for each in dataset['female sentences']:
        sen_temp = sentimentanalyzer(each)[0]
        if sen_temp['label'] == 'POSITIVE':
            female_sentiment.append(sen_temp['score'])
        elif sen_temp['label'] == 'NEGATIVE':
            female_sentiment.append(0 - sen_temp['score'])
        else:
            female_sentiment.append(sen_temp['score'])

    k = 0
    female_averages = []
    for m in range(40):
        total = 0
        for each in female_sentiment[k:k+10]:
            total = total + each
        average = total / 10
        female_averages.append(round(average,2))
        k = k+10

    if (token==0):
        out = pd.read_csv('../../data/baseline/sentence-level/sentence_level_averages.csv')
        out['male_dbert_average'] = male_averages
        out['female_dbert_average'] =  female_averages
        out.to_csv('../../data/baseline/sentence-level/sentence_level_averages.csv',index=False)
    else:
        out = pd.read_csv('../../data/baseline/sentence-level/sentence_level_averages_name.csv')
        out['male_dbert_average'] = male_averages
        out['female_dbert_average'] =  female_averages
        out.to_csv('../../data/baseline/sentence-level/sentence_level_averages_name.csv',index=False)
