import sys




def run_bf():
    sys.path.insert(1, 'sentiment-models/biased/')
    import bf
    print("Generating results from bf SAS...")
    bf.allure_data("../data/real-world/allure/final/final.csv")

def run_textblob():
    sys.path.insert(1, 'sentiment-models/textblob/')
    import textblob_sas
    print("Generating results from Textblob SAS...")
    textblob_sas.allure_data("../data/real-world/allure/final/final.csv")


def run_dbert():
    sys.path.insert(1, 'sentiment-models/DistilBERT/')
    import dbert_sas
    print("Generating results from DistilBERT SAS...")
    dbert_sas.allure_data("../data/real-world/allure/final/final.csv")
    

def run_random():
    sys.path.insert(1, 'sentiment-models/random_sas/')
    import random_sas
    print("Generating results from random SAS...")
    random_sas.allure_data("../data/real-world/allure/final/final.csv")


def run_gru():
    sys.path.insert(1, 'sentiment-models/gru/')
    import ClassificationGRU
    print("Generating results from GRU SAS...")
    ClassificationGRU.allure_data("../data/real-world/allure/final/final.csv")
    

print("Generating results from different SASs for the data \n")
run_bf()
run_gru()
run_random()
run_textblob()
run_dbert()
