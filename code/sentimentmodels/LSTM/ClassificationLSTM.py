from nltk.corpus import stopwords
import pandas as pd
import re
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
import pickle
import numpy as np
import tensorflow as tf
tf.get_logger().setLevel('INFO')
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense,GRU,LSTM,Embedding
from keras.optimizers import Adam
from keras.layers import SpatialDropout1D,Dropout,Bidirectional,Conv1D,GlobalMaxPooling1D,MaxPooling1D,Flatten
from keras.callbacks import ModelCheckpoint, TensorBoard, Callback, EarlyStopping



def lstm_sentiment(path, file_name):

    with open('./LSTM/tokenizer.pickle', 'rb') as h:
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



    model3_LSTM = keras.models.load_model("./LSTM/checkpoints/")

    pred = model3_LSTM.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)

    print("Different sentiment values are:" ,set(sentiment_norm))

    d = {'Sentence':eec,'Sentiment':sentiment_norm, 'Gender':gender}
    final_df = pd.DataFrame(d, columns=['Sentence','Sentiment','Gender'])
    final_df.to_csv('../../data/results/lstm/nonames/{}.csv'.format(file_name))


def lstm_sentiment_name(path, file_name):

    with open('./LSTM/tokenizer.pickle', 'rb') as h:
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



    model3_LSTM = keras.models.load_model("./LSTM/checkpoints/")

    pred = model3_LSTM.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)

    print("Different sentiment values are:" ,set(sentiment_norm))

    d = {'Sentence':eec,'Sentiment':sentiment_norm, 'Gender':gender}
    final_df = pd.DataFrame(d, columns=['Sentence','Sentiment','Gender'])
    final_df.to_csv('../../data/results/lstm/withnames/{}.csv'.format(file_name))

def lstm_sentiment_baseline(path):

    with open('./LSTM/tokenizer.pickle', 'rb') as h:
        tokenizer = pickle.load(h)

    eec_data = pd.read_csv(path,engine="python")
    max_words = 50

    eec = []
    for each in eec_data['Sentences']:
        eec.append(each)


    data = tokenizer.texts_to_sequences(eec)
    data = pad_sequences(data, maxlen=max_words)



    model3_LSTM = keras.models.load_model("./LSTM/checkpoints/")

    pred = model3_LSTM.predict(data, verbose=1)
    #sentiment = np.amax(pred,1)
    sentiment = pred.argmax(axis=1)

    #Normalizing the sentiment scores.
    sentiment_norm = []
    for each in sentiment:
        sentiment_norm.append((each-3)/3)

    print("Different sentiment values are:" ,set(sentiment_norm))

    eec_data['Sentiment_lstm'] = sentiment_norm
    eec_data.to_csv(path,index=False)
