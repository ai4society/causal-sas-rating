from textblob import TextBlob
import nltk
import pandas as pd


"""
Input: path for dataset which is to be analyzed,
       name with which the result should be stored.
Output: Result datasets will be generated.
"""
def textblobsentiment(path,file_name):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        sentiment.append(each.sentiment[0])
    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])

    final_df.to_csv('../../data/results/textblob/nonames/{}.csv'.format(file_name))

def textblobsentiment_name(path,file_name):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        sentiment.append(each.sentiment[0])
    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])

    final_df.to_csv('../../data/results/textblob/withnames/{}.csv'.format(file_name))

def textblobsentiment_baseline(path):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        sentiment.append(each.sentiment[0])
    text = []
    for each in set['Sentences']:
        text.append(each)

    set['Sentiment_textblob'] = sentiment
    set.to_csv(path,index=False)


def textblobsentiment_sentence_baseline(path):
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
    male_senti = []
    for each in dataset['male sentences']:
        male_senti.append(TextBlob(each))

    male_sentiment = []
    for each in male_senti:
        male_sentiment.append(each.sentiment[0])

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

    female_senti = []
    for each in dataset['female sentences']:
        female_senti.append(TextBlob(each))

    female_sentiment = []
    for each in female_senti:
        female_sentiment.append(each.sentiment[0])

    k = 0
    female_averages = []
    for m in range(40):
        total = 0
        for each in female_sentiment[k:k+10]:
            total = total + each
        average = total / 10
        female_averages.append(round(average,2))
        k = k+10

    templates = []
    templates_num = []
    for m in range(10):
        for k in range(4):
             templates_num.append("s{}".format(k+1))
             templates.append(template[k])


    for each_em in emotion_words:
        for k in range(4):
            words.append(each_em)

    (pd.DataFrame.from_dict({'word':words,'sentence':templates,'sentence number':templates_num,'male_textblob_average':male_averages,'female_textblob_average':female_averages})).to_csv('../../data/baseline/sentence-level/sentence_level_averages.csv',index=False)
