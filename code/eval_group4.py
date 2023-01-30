import sys


def run_bf():
    sys.path.insert(1, 'sentiment-models/biased/')
    import bf
    print("Generating results from bf SAS...")
    bf.g4("../data/data-generated/group4/e3.csv", 2)


def run_gru():
    sys.path.insert(1, 'sentiment-models/gru/')
    import ClassificationGRU
    print("Generating results from GRU SAS...")
    ClassificationGRU.g4("../data/data-generated/group4/e3.csv",2,0)
    ClassificationGRU.g4("../data/data-generated/group4/e3.csv",2,1)


def run_random():
    sys.path.insert(1, 'sentiment-models/random_sas/')
    import random_sas
    print("Generating results from random SAS...")
    random_sas.g4("../data/data-generated/group4/e3.csv",2)


def run_textblob():
    sys.path.insert(1, 'sentiment-models/textblob/')
    import textblob_sas
    print("Generating results from Textblob SAS...")
    textblob_sas.g4("../data/data-generated/group4/e3.csv",2,0)
    textblob_sas.g4("../data/data-generated/group4/e3.csv",2,1)


def run_dbert():
    sys.path.insert(1, 'sentiment-models/DistilBERT/')
    import dbert_sas
    print("Generating results from DistilBERT SAS...")
    dbert_sas.g4("../data/data-generated/group4/e3.csv",2)

# for i in range(1,6):
print("Generating results from different SASs for e3")
run_bf()
# run_gru()
run_random()
run_textblob()
run_dbert()
