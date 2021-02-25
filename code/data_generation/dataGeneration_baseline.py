import pandas as pd
import random

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


for each_em_word in emotion_words:
    sentences = []

    for k in range(len(template)):
        sentences.append(template[k].replace("<emotion word>",each_em_word))

    sentences = list(sentences)
    final_sentences = []
    for m,f in zip(male,female):
        for each in sentences:
            final_sentences.append(each.replace("<person object>",m).replace("<person subject>",m))
            final_sentences.append(each.replace("<person object>",f).replace("<person subject>",f))

    (pd.DataFrame.from_dict({'Sentences':final_sentences})).to_csv('../../data/baseline/{}_sentiment.csv'.format(each_em_word),index=False)
