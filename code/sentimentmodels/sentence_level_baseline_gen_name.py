import pandas as pd
import random
from TextBlob import textblob
from Vader import vader
from CNNforNLP import cnn
from LSTM import ClassificationLSTM
from GRU import ClassificationGRU
from TextBlob_French import test
from DistilBERT import dbert
import argparse

original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

template = sorted(set(original_data['Template']))
template = list([template[0],template[4],template[6],template[10]])

male = list(sorted(set(original_data[original_data['Gender']=='male']['Person'])))[:10]
female = list(sorted(set(original_data[original_data['Gender']=='female']['Person'])))[:10]

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)

emotion_words = [emo[21],emo[22],emo[4],emo[30],emo[6],emo[16],emo[3],emo[18],emo[28],emo[12]]

file_count = 0


male_sentences = []
female_sentences = []
pair_name = []
word = []
male_sentiment = []
female_sentiment = []


for each_em_word in emotion_words:
    for k in range(len(template)):
        for m in male:
            male_sentences.append(template[k].replace("<person object>",m).replace("<person subject>",m).replace("<emotion word>",each_em_word))
        for f in female:
            female_sentences.append(template[k].replace("<person object>",f).replace("<person subject>",f).replace("<emotion word>",each_em_word))


(pd.DataFrame.from_dict({'male sentences':male_sentences, 'female sentences':female_sentences})).to_csv('../../data/baseline/sentence-level/sentences_name.csv',index=False)

def run_blob():
    textblob.textblobsentiment_sentence_baseline("../../data/baseline/sentence-level/sentences_name.csv",1)

    print("Results from TextBlob have been generated at:../../data/baseline/sentence-level/ ")

def run_cnn():
    cnn.cnnsentiment_sentence_baseline("../../data/baseline/sentence-level/sentences_name.csv",1)

    print("Results from CNN have been generated at: ../../data/baseline/sentence-level/")

def run_dbert():
    dbert.bertsentiment_sentence_baseline("../../data/baseline/sentence-level/sentences_name.csv",1)
    print("Results from DistilBERT have been generated at:../../data/baseline/sentence-level/ ")

def run_gru():
    ClassificationGRU.gru_sentence_baseline("../../data/baseline/sentence-level/sentences_name.csv",1)
    print("Results from GRU have been generated at: ../../data/baseline/sentence-level/")

def run_lstm():
    ClassificationLSTM.lstm_sentence_baseline("../../data/baseline/sentence-level/sentences_name.csv",1)
    print("Results from LSTM have been generated at: ../../data/baseline/sentence-level/")

def run_vader():
    vader.vadersentiment_sentence_baseline("../../data/baseline/sentence-level/sentences_name.csv",1)
    print("Results from VADER have been generated at: ../../data/baseline/sentence-level/")

run_blob()
run_cnn()
run_dbert()
run_gru()
run_lstm()
run_vader()
