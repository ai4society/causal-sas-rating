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
