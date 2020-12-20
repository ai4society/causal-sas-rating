
import numpy as np
import math
import re
import pandas as pd
from bs4 import BeautifulSoup
import pickle

import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds

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

    def __init__(self,
                 vocab_size,
                 emb_dim=128,
                 nb_filters=50,
                 FFN_units=512,
                 nb_classes=2,
                 dropout_rate=0.1,
                 training=False,
                 name="dcnn"):
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

        merged = tf.concat([x_1, x_2, x_3], axis=-1) # (batch_size, 3 * nb_filters)
        merged = self.dense_1(merged)
        merged = self.dropout(merged, training)
        output = self.last_dense(merged)

        return output

#All the parameters we will be using.
VOCAB_SIZE = tokenizer.vocab_size

EMB_DIM = 200
NB_FILTERS = 100
FFN_UNITS = 256
NB_CLASSES = 2#len(set(train_labels))

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
        sentiment.append(Dcnn(np.array([tokenizer.encode(each)]), training=False).numpy())

    d = {'Sentence':set['Sentences'],'Sentiment':sentiment,'Gender':set['Gender']}
    final_df = pd.DataFrame(d, columns=['Sentence','Sentiment','Gender'])
    final_df.to_csv('../../data/results/cnn/{}.csv'.format(file_name))
