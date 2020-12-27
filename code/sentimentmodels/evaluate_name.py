from TextBlob import textblob
from Vader import vader
from CNNforNLP import cnn
import argparse



def run_blob():
    for i in range(1,6):
        print("Generating TextBlob set {}/5...".format(i))
        textblob.textblobsentiment_name("../../data/data-generated/withnames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        textblob.textblobsentiment_name("../../data/data-generated/withnames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        textblob.textblobsentiment_name("../../data/data-generated/withnames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from TextBlob have been generated at:  '../../data/results/textblob/withnames/'")


def run_vader():
    for i in range(1,6):
        print("Generating Vader set {}/5...".format(i))
        vader.vadersentiment_name("../../data/data-generated/withnames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        vader.vadersentiment_name("../../data/data-generated/withnames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        vader.vadersentiment_name("../../data/data-generated/withnames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from Vader have been generated at:  '../../data/results/vader/withnames/'")

def run_cnn():
    for i in range(1,6):
        print("Generating CNN set {}/5...".format(i))
        cnn.cnnsentiment_name("../../data/data-generated/withnames/u{}.csv".format(i),"result_p{}_u_.5_.5".format(i))
        cnn.cnnsentiment_name("../../data/data-generated/withnames/bf{}.csv".format(i),"result_p{}_b_.1_.9".format(i))
        cnn.cnnsentiment_name("../../data/data-generated/withnames/bm{}.csv".format(i),"result_p{}_b_.9_.1".format(i))
    print("Results from CNN have been generated at:  '../../data/results/cnn/withnames/'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model',required = True, help="Either of these sentiment analyzers: textblob, vader or cnn")
    args = parser.parse_args()

    if args.model == "vader":
        run_vader()
    if args.model == "textblob":
        run_blob()
    if args.model == "cnn":
        run_cnn()
