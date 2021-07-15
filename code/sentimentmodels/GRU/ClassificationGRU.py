from nltk.corpus import stopwords
import pandas as pd
import re
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
import pickle
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import tensorflow as tf
from tensorflow import keras

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense,GRU,LSTM,Embedding
from keras.optimizers import Adam
from keras.layers import SpatialDropout1D,Dropout,Bidirectional,Conv1D,GlobalMaxPooling1D,MaxPooling1D,Flatten
from keras.callbacks import ModelCheckpoint, TensorBoard, Callback, EarlyStopping



def gru_sentiment(path,file_name):

    with open('./GRU/tokenizer.pickle', 'rb') as h:
        tokenizer = pickle.load(h)

    eec_data = pd.read_csv(path,engine="python")
    max_words = 50

    eec = []
    for each in eec_data['Sentences']:
        eec.append(each)
    gender = []
    for each in eec_data['Gender']:
        gender.append(each)

    data = tokenizer.texts_to_sequences(eec)
    data = pad_sequences(data, maxlen=max_words)



    model_GRU = keras.models.load_model("./GRU/checkpoints/")

    pred = model_GRU.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)


    print("Different sentiment values are:" ,set(sentiment_norm))

    d = {'Sentence':eec,'Sentiment':sentiment_norm, 'Gender':gender}
    final_df = pd.DataFrame(d, columns=['Sentence','Sentiment','Gender'])
    final_df.to_csv('../../data/results/gru/nonames/{}.csv'.format(file_name))

def gru_sentiment_name(path,file_name):

    with open('./GRU/tokenizer.pickle', 'rb') as h:
        tokenizer = pickle.load(h)

    eec_data = pd.read_csv(path,engine="python")
    max_words = 50

    eec = []
    for each in eec_data['Sentences']:
        eec.append(each)
    gender = []
    for each in eec_data['Gender']:
        gender.append(each)

    data = tokenizer.texts_to_sequences(eec)
    data = pad_sequences(data, maxlen=max_words)



    model_GRU = keras.models.load_model("./GRU/checkpoints/")

    pred = model_GRU.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)


    print("Different sentiment values are:" ,set(sentiment_norm))

    d = {'Sentence':eec,'Sentiment':sentiment_norm, 'Gender':gender}
    final_df = pd.DataFrame(d, columns=['Sentence','Sentiment','Gender'])
    final_df.to_csv('../../data/results/gru/withnames/{}.csv'.format(file_name))

def gru_sentiment_baseline(path):

    with open('./GRU/tokenizer.pickle', 'rb') as h:
        tokenizer = pickle.load(h)

    eec_data = pd.read_csv(path,engine="python")
    max_words = 50

    eec = []
    for each in eec_data['Sentences']:
        eec.append(each)


    data = tokenizer.texts_to_sequences(eec)
    data = pad_sequences(data, maxlen=max_words)

    model_GRU = keras.models.load_model("./GRU/checkpoints/")

    pred = model_GRU.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)


    print("Different sentiment values are:" ,set(sentiment_norm))

    eec_data['Sentiment_gru'] = sentiment_norm
    eec_data.to_csv(path,index=False)




def gru_sentence_baseline(path):
    with open('./GRU/tokenizer.pickle', 'rb') as h:
        tokenizer = pickle.load(h)

    max_words = 50

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
    model_GRU = keras.models.load_model("./GRU/checkpoints/")

    male_sentences_seq = tokenizer.texts_to_sequences(dataset['male sentences'])
    male_sentences_seq = pad_sequences(male_sentences_seq, maxlen=max_words)

    female_sentences_seq = tokenizer.texts_to_sequences(dataset['female sentences'])
    female_sentences_seq = pad_sequences(female_sentences_seq, maxlen=max_words)

    male_pred = model_GRU.predict(male_sentences_seq, verbose=1)
    female_pred = model_GRU.predict(female_sentences_seq, verbose=1)

    male_sentiment = male_pred.argmax(axis=1)
    female_sentiment = female_pred.argmax(axis=1)
    #Normalizing the sentiment scores.
    male_sentiment_norm = []
    female_sentiment_norm = []
    for each in male_sentiment:
        male_sentiment_norm.append((each-3)/3)

    for each in female_sentiment:
        female_sentiment_norm.append((each-3)/3)

    k = 0
    male_averages = []
    for m in range(40):
        total = 0
        for each in male_sentiment_norm[k:k+10]:
            total = total + each
        average = total / 10
        male_averages.append(round(average,2))
        k = k+10
    print(len(male_averages))

    k = 0
    female_averages = []
    for m in range(40):
        total = 0
        for each in female_sentiment_norm[k:k+10]:
            total = total + each
        average = total / 10
        female_averages.append(round(average,2))
        k = k+10

    out = pd.read_csv('../../data/baseline/sentence-level/sentence_level_averages.csv')
    out['male_gru_average'] = male_averages
    out['female_gru_average'] =  female_averages
    out.to_csv('../../data/baseline/sentence-level/sentence_level_averages.csv',index=False)
