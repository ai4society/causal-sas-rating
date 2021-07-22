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

    final_df.to_csv('../../data/results/vader/nonames/{}.csv'.format(file_name))

def vadersentiment_name(path,file_name):
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

    final_df.to_csv('../../data/results/vader/withnames/{}.csv'.format(file_name))

def vadersentiment_baseline(path):
    #Loading the dataset
    set = pd.read_csv(path,engine="python")
    #Seperating sentence,race and gender into lists.
    eec = []
    for each in set['Sentences']:
        eec.append(each)

    sentiment = []
    for each in eec:
        sentiment.append(sentiment_rating(each)['compound'])

    set['Sentiment_vader'] = sentiment
    set.to_csv(path,index=False)

def vadersentiment_sentence_baseline(path,token):
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
        male_sentiment.append(sentiment_rating(each)['compound'])

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
        female_sentiment.append(sentiment_rating(each)['compound'])

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
        out['male_vader_average'] = male_averages
        out['female_vader_average'] =  female_averages
        out.to_csv('../../data/baseline/sentence-level/sentence_level_averages.csv',index=False)
    else:
        out = pd.read_csv('../../data/baseline/sentence-level/sentence_level_averages_name.csv')
        out['male_vader_average'] = male_averages
        out['female_vader_average'] =  female_averages
        out.to_csv('../../data/baseline/sentence-level/sentence_level_averages_name.csv',index=False)
