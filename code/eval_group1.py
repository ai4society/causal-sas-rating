import sys


def run_bf(i):
    sys.path.insert(1, 'sentiment-models/biased/')
    import bf
    print("Generating results from bf SAS...")
    bf.g1("../data/data-generated/group1/e{}.csv".format(i),i,1)


def run_gru(i):
    sys.path.insert(1, 'sentiment-models/gru/')
    import ClassificationGRU
    print("Generating results from GRU SAS...")
    # ClassificationGRU.g1("../data/data-generated/group1/e{}.csv".format(i),i,1,0)
    ClassificationGRU.g1("../data/data-generated/group1/e{}.csv".format(i),i,1,1)


def run_random(i):
    sys.path.insert(1, 'sentiment-models/random_sas/')
    import random_sas
    print("Generating results from random SAS...")
    random_sas.g1("../data/data-generated/group1/e{}.csv".format(i),i,1)


def run_textblob(i):
    sys.path.insert(1, 'sentiment-models/textblob/')
    import textblob_sas
    print("Generating results from Textblob SAS...")
    # textblob_sas.g1("../data/data-generated/group1/e{}.csv".format(i),i,1,0)
    textblob_sas.g1("../data/data-generated/group1/e{}.csv".format(i),i,1,1)



def run_dbert(i):
    sys.path.insert(1, 'sentiment-models/DistilBERT/')
    import dbert_sas
    print("Generating results from DistilBERT SAS...")
    dbert_sas.g1("../data/data-generated/group1/e{}.csv".format(i),i,1)

for i in range(1,6):
    print("Generating results from different SASs for e{}".format(i))
    # run_bf(i)
    run_gru(i)
    # run_random(i)
    run_textblob(i)
    # run_dbert(i)
