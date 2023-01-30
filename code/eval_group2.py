import sys


def run_bf():
    sys.path.insert(1, 'sentiment-models/biased/')
    import bf
    print("Generating results from bf SAS...")
    bf.g2("../data/data-generated/group2/e3.csv",1)


def run_gru():
    sys.path.insert(1, 'sentiment-models/gru/')
    import ClassificationGRU
    print("Generating results from GRU SAS...")
    # ClassificationGRU.g2("../data/data-generated/group2/e3.csv",1,0)
    ClassificationGRU.g2("../data/data-generated/group2/e3.csv",1,1)


def run_random():
    sys.path.insert(1, 'sentiment-models/random_sas/')
    import random_sas
    print("Generating results from random SAS...")
    random_sas.g2("../data/data-generated/group2/e3.csv",1)


def run_textblob():
    sys.path.insert(1, 'sentiment-models/textblob/')
    import textblob_sas
    print("Generating results from Textblob SAS...")
    # textblob_sas.g2("../data/data-generated/group2/e3.csv",1,0)
    textblob_sas.g2("../data/data-generated/group2/e3.csv",1,1)


def run_dbert():
    sys.path.insert(1, 'sentiment-models/DistilBERT/')
    import dbert_sas
    print("Generating results from DistilBERT SAS...")
    dbert_sas.g2("../data/data-generated/group2/e3.csv",1)


print("Generating results from different SASs for e3")
# run_bf()
run_gru()
# run_random()
run_textblob()
# run_dbert()
