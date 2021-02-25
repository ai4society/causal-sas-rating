from TextBlob import textblob
from Vader import vader
from CNNforNLP import cnn
from LSTM import ClassificationLSTM
from GRU import ClassificationGRU
from TextBlob_French import test
from DistilBERT import dbert
import argparse
import pandas as pd

original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)

emotion_words = [emo[21],emo[22],emo[4],emo[30],emo[6],emo[16],emo[3],emo[18],emo[28],emo[12]]

def run_blob():
    for word in emotion_words:
        textblob.textblobsentiment_baseline("../../data/baseline/{}_sentiment.csv".format(word))

    print("Results from TextBlob have been generated at:  '../../data/baseline/'")



def run_vader():
    for word in emotion_words:
        vader.vadersentiment_baseline("../../data/baseline/{}_sentiment.csv".format(word))

    print("Results from Vader have been generated at:  '../../data/baseline/'")


def run_cnn():
    for word in emotion_words:
        cnn.cnnsentiment_baseline("../../data/baseline/{}_sentiment.csv".format(word))

    print("Results from CNN have been generated at:  '../../data/baseline/'")

def run_lstm():
    for word in emotion_words:
        ClassificationLSTM.lstm_sentiment_baseline("../../data/baseline/{}_sentiment.csv".format(word))

    print("Results from LSTM have been generated at:  '../../data/baseline/'")

def run_gru():
    for word in emotion_words:
        ClassificationGRU.gru_sentiment_baseline("../../data/baseline/{}_sentiment.csv".format(word))

    print("Results from LSTM have been generated at:  '../../data/baseline/'")

def run_dbert():
    for word in emotion_words:
        dbert.bertsentiment_baseline("../../data/baseline/{}_sentiment.csv".format(word))

    print("Results from LSTM have been generated at:  '../../data/baseline/'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model',required = True, help="Either of these sentiment analyzers: textblob, vader, cnn, lstm, gru, dbert, textblob_fr or textblob_fr_oto")
    args = parser.parse_args()

    if args.model == "vader":
        run_vader()
    if args.model == "textblob":
        run_blob()
    if args.model == "cnn":
        run_cnn()
    if args.model == "lstm":
        run_lstm()
    if args.model == "gru":
        run_gru()
    if args.model == "dbert":
        run_dbert()
    if args.model == "all":
        run_vader()
        run_blob()
        run_cnn()
        run_lstm()
        run_gru()
        run_dbert()
