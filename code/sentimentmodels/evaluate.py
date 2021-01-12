from TextBlob import textblob
from Vader import vader
from CNNforNLP import cnn
from LSTM import ClassificationLSTM
from GRU import ClassificationGRU
import argparse



def run_blob():
    for i in range(1,6):
        print("Generating TextBlob set {}/5...".format(i))
        textblob.textblobsentiment("../../data/data-generated/nonames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        textblob.textblobsentiment("../../data/data-generated/nonames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        textblob.textblobsentiment("../../data/data-generated/nonames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from TextBlob have been generated at:  '../../data/results/textblob/nonames/'")


def run_vader():
    for i in range(1,6):
        print("Generating Vader set {}/5...".format(i))
        vader.vadersentiment("../../data/data-generated/nonames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        vader.vadersentiment("../../data/data-generated/nonames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        vader.vadersentiment("../../data/data-generated/nonames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from Vader have been generated at:  '../../data/results/vader/nonames/'")

def run_cnn():
    for i in range(1,6):
        print("Generating CNN set {}/5...".format(i))
        cnn.cnnsentiment("../../data/data-generated/nonames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        cnn.cnnsentiment("../../data/data-generated/nonames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        cnn.cnnsentiment("../../data/data-generated/nonames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from CNN have been generated at:  '../../data/results/cnn/nonames/'")

def run_lstm():
    for i in range(1,6):
        print("Generating LSTM set {}/5...".format(i))
        ClassificationLSTM.lstm_sentiment("../../data/data-generated/nonames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        ClassificationLSTM.lstm_sentiment("../../data/data-generated/nonames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        ClassificationLSTM.lstm_sentiment("../../data/data-generated/nonames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from LSTM have been generated at:  '../../data/results/lstm/nonames/'")

def run_gru():
    for i in range(1,6):
        print("Generating GRU set {}/5...".format(i))
        ClassificationGRU.gru_sentiment("../../data/data-generated/nonames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        ClassificationGRU.gru_sentiment("../../data/data-generated/nonames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        ClassificationGRU.gru_sentiment("../../data/data-generated/nonames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from GRU have been generated at:  '../../data/results/lstm/nonames/'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model',required = True, help="Either of these sentiment analyzers: textblob, vader, cnn, lstm or gru")
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
