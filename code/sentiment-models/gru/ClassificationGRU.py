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
# from keras.io.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense,GRU,LSTM,Embedding
from keras.optimizers import Adam
from keras.layers import SpatialDropout1D,Dropout,Bidirectional,Conv1D,GlobalMaxPooling1D,MaxPooling1D,Flatten
from keras.callbacks import ModelCheckpoint, TensorBoard, Callback, EarlyStopping


# 'c' is a flag which tells whether the sentiment is binary or continuous attribute.
def gru_sentiment(path,k,c):

    with open('./sentiment-models/gru/tokenizer.pickle', 'rb') as h:
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
    data = keras.preprocessing.sequence.pad_sequences(data, maxlen=max_words)



    model_GRU = keras.models.load_model("./sentiment-models/gru/checkpoints/")

    pred = model_GRU.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)

    sen = []

    for each in sentiment_norm:
        if each >= 0:
            sen.append(1)
        elif each < 0:
            sen.append(0)
    
    # For non-binary sentiment,
    if c == 1:
        sen = sentiment_norm


    g1 = {'Gender':gender,'Emotion':eec_data['Emotion'], 'Sentiment':sen}

    if k == 2:
        g2 = {'Gender':gender,'Race':eec_data['Race'],'Emotion':eec_data['Emotion'],'Sentiment':sen}
        return g2
    elif k == 1:
        return g1




def g1(path,i,k,c):

    df = gru_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c==0:
        final_df.to_csv('../data/results/group1/gru/e{}_gru.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group1/gru/e{}_gru.csv'.format(i),index=False)


def g2(path,k,c):

    df = gru_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group2/gru/e3_gru.csv',index=False)
    else:
        final_df.to_csv('../data/results/continuous/group2/gru/e3_gru.csv',index=False)
        

def g3(path,i,k,c):

    df = gru_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group3/gru/e{}_gru.csv'.format(i),index=False)
    else:
        final_df.to_csv('../data/results/continuous/group3/gru/e{}_gru.csv'.format(i),index=False)


def g4(path,k,c):

    df = gru_sentiment(path,k,c)
    final_df = pd.DataFrame(df, columns=['Gender','Race','Emotion','Sentiment'])
    if c == 0:
        final_df.to_csv('../data/results/group4/gru/e3_gru.csv',index=False)
    else:
        final_df.to_csv('../data/results/continuous/group4/gru/e3_gru.csv',index=False)
