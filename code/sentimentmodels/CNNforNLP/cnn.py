
import numpy as np
import math
import re
import pandas as pd
from bs4 import BeautifulSoup
import pickle

import tensorflow as tf
from tensorflow.keras import layers
# import tensorflow_datasets as tfds
# import sys
# sys.path.insert(0,'.')
with open('./CNNforNLP/tokenizer.pickle', 'rb') as h:
    tokenizer = pickle.load(h)

#Our CNN network.
"""
Inputs : vocab_size given by us in the tokenizer part, Embedding size (128 is taken in most of the cases),
         For each of our filter we take 50 units, Feedforward network units,
         dropout rate(For regularization only during training),
         Boolean training indicates whether it is training or testing.
"""
class DCNN(tf.keras.Model):

    def __init__(self,vocab_size,emb_dim=128,nb_filters=50,FFN_units=512,nb_classes=2,dropout_rate=0.1,training=False,name="dcnn"):

        super(DCNN, self).__init__(name=name)

        self.embedding = layers.Embedding(vocab_size,
                                          emb_dim)
        self.bigram = layers.Conv1D(filters=nb_filters,
                                    kernel_size=2,
                                    padding="valid",
                                    activation="relu")
        self.trigram = layers.Conv1D(filters=nb_filters,
                                     kernel_size=3,
                                     padding="valid",
                                     activation="relu")
        self.fourgram = layers.Conv1D(filters=nb_filters,
                                      kernel_size=4,
                                      padding="valid",
                                      activation="relu")
        self.pool = layers.GlobalMaxPool1D() # no training variable so we can
                                             # use the same layer for each
                                             # pooling step
        self.dense_1 = layers.Dense(units=FFN_units, activation="relu")
        self.dropout = layers.Dropout(rate=dropout_rate)
        if nb_classes == 2:
            self.last_dense = layers.Dense(units=1,
                                           activation="sigmoid")
        else:
            self.last_dense = layers.Dense(units=nb_classes,
                                           activation="softmax")

    def call(self, inputs, training):
        x = self.embedding(inputs)
        x_1 = self.bigram(x)
        x_1 = self.pool(x_1)
        x_2 = self.trigram(x)
        x_2 = self.pool(x_2)
        x_3 = self.fourgram(x)
        x_3 = self.pool(x_3)

        merged = tf.concat([x_1, x_2, x_3], axis=-1) # (batch_size, 3 * no. of filters)
        merged = self.dense_1(merged)
        merged = self.dropout(merged, training)
        output = self.last_dense(merged)

        return output

#All the parameters we will be using.
VOCAB_SIZE = tokenizer.vocab_size

EMB_DIM = 200
NB_FILTERS = 100
FFN_UNITS = 256
NB_CLASSES = 2

DROPOUT_RATE = 0.2

BATCH_SIZE = 32
NB_EPOCHS = 5

#Initializing our network.
Dcnn = DCNN(vocab_size=VOCAB_SIZE,
            emb_dim=EMB_DIM,
            nb_filters=NB_FILTERS,
            FFN_units=FFN_UNITS,
            nb_classes=NB_CLASSES,
            dropout_rate=DROPOUT_RATE)


Dcnn.compile(loss="binary_crossentropy",optimizer="adam",metrics=["accuracy"])
"""
Saving the checkpoint after training.
If the checkpoint exists we restore it.
"""
checkpoint_path = "./CNNforNLP/checkpoints/"

ckpt = tf.train.Checkpoint(Dcnn=Dcnn)

ckpt_manager = tf.train.CheckpointManager(ckpt, checkpoint_path, max_to_keep=5)

if ckpt_manager.latest_checkpoint:
    ckpt.restore(ckpt_manager.latest_checkpoint)
    print("Latest checkpoint restored!!")



def cnnsentiment(path,file_name):
    set = pd.read_csv(path,engine="python")
    sentiment = []

    for each in set['Sentences']:
        #Scaling it to be between -1 to 1 after getting the result.
        # new_value = (((old_value - old_min)/(old_max - old_min))*(new_max-new_min)) + new_min
        sentiment.append(2 * ((Dcnn(np.array([tokenizer.encode(each)]), training=False).numpy())[0][0]) - 1)

    d = {'Sentence':set['Sentences'],'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])
    final_df.to_csv('../../data/results/cnn/nonames/{}.csv'.format(file_name))

def cnnsentiment_name(path,file_name):
    set = pd.read_csv(path,engine="python")
    sentiment = []

    for each in set['Sentences']:
        #Scaling it to be between -1 to 1 after getting the result.
        # new_value = (((old_value - old_min)/(old_max - old_min))*(new_max-new_min)) + new_min
        sentiment.append(2 * ((Dcnn(np.array([tokenizer.encode(each)]), training=False).numpy())[0][0]) - 1)

    d = {'Sentence':set['Sentences'],'Gender':set['Gender'],'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])
    final_df.to_csv('../../data/results/cnn/withnames/{}.csv'.format(file_name))

def cnnsentiment_baseline(path):
    set = pd.read_csv(path,engine="python")
    sentiment = []

    for each in set['Sentences']:
        #Scaling it to be between -1 to 1 after getting the result.
        # new_value = (((old_value - old_min)/(old_max - old_min))*(new_max-new_min)) + new_min
        sentiment.append(2 * ((Dcnn(np.array([tokenizer.encode(each)]), training=False).numpy())[0][0]) - 1)


    set['Sentiment_cnn'] = sentiment
    set.to_csv(path,index=False)

def cnnsentiment_sentence_baseline(path):
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
        male_sentiment.append(2 * ((Dcnn(np.array([tokenizer.encode(each)]), training=False).numpy())[0][0]) - 1)


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
        female_sentiment.append(2 * ((Dcnn(np.array([tokenizer.encode(each)]), training=False).numpy())[0][0]) - 1)

    k = 0
    female_averages = []
    for m in range(40):
        total = 0
        for each in female_sentiment[k:k+10]:
            total = total + each
        average = total / 10
        female_averages.append(round(average,2))
        k = k+10



    out = pd.read_csv('../../data/baseline/sentence-level/sentence_level_averages.csv')
    out['male_cnn_average'] = male_averages
    out['female_cnn_average'] =  female_averages
    out.to_csv('../../data/baseline/sentence-level/sentence_level_averages.csv',index=False)
