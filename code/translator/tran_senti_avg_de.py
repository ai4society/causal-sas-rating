import pandas as pd

#Calculating the average sentiment scores for French to OTO dataset.
def calc_averages_de_oto():
    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu1_oto = (sum/240)
    print("Average sentiment score for pair-1 of OTO dataset from German without names is",round(wpu1_oto,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu2_oto = (sum/240)
    print("Average sentiment score for pair-2 of OTO dataset from German without names is",round(wpu2_oto,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu3_oto = (sum/240)
    print("Average sentiment score for pair-3 of OTO dataset from German without names is",round(wpu3_oto,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu4_oto = (sum/240)
    print("Average sentiment score for pair-3 of OTO dataset from German without names is",round(wpu4_oto,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu5_oto = (sum/240)
    print("Average sentiment score for pair-3 of OTO dataset from German without names is",round(wpu5_oto,2))

    return [wpu1_oto,wpu2_oto,wpu3_oto,wpu4_oto,wpu5_oto]

##Calculating average sentiment scores for German dataset
def calc_averages_de():

    pa = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu1_fr = (sum/240)
    print("Average sentiment score for pair-1 of German dataset without names is",round(wpu1_fr,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu2_fr = (sum/240)
    print("Average sentiment score for pair-2 of French dataset without names is",round(wpu2_fr,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu3_fr = (sum/240)
    print("Average sentiment score for pair-3 of German dataset without names is",round(wpu3_fr,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu4_fr = (sum/240)
    print("Average sentiment score for pair-3 of German dataset without names is",round(wpu4_fr,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu5_fr = (sum/240)
    print("Average sentiment score for pair-3 of German dataset without names is",round(wpu5_fr,2))

    return [wpu1_fr,wpu2_fr,wpu3_fr,wpu4_fr,wpu5_fr]

##Average sentiment scores for English dataset.
def calc_averages_en():
    pa = pd.read_csv("../../data/results/textblob/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu1_en = (sum/240)
    print("Average sentiment score for pair-1 of original English dataset without names is",round(wpu1_en,2))

    pa = pd.read_csv("../../data/results/textblob/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu2_en = (sum/240)
    print("Average sentiment score for pair-2 of original English dataset without names is",round(wpu2_en,2))

    pa = pd.read_csv("../../data/results/textblob/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu3_en = (sum/240)
    print("Average sentiment score for pair-3 of original English dataset without names is",round(wpu3_en,2))

    pa = pd.read_csv("../../data/results/textblob/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu4_en = (sum/240)
    print("Average sentiment score for pair-3 of original English dataset without names is",round(wpu4_en,2))

    pa = pd.read_csv("../../data/results/textblob/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu5_en = (sum/240)
    print("Average sentiment score for pair-3 of original English dataset without names is",round(wpu5_en,2))

    return [wpu1_en,wpu2_en,wpu3_en,wpu4_en,wpu5_en]

##Average sentiment scores for French to OTO dataset with names.
def calc_averages_de_oto_n():
    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu1_oto_n = (sum/240)
    print("Average sentiment score for pair-1 of OTO dataset from German with names is",round(wpu1_oto_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu2_oto_n = (sum/240)
    print("Average sentiment score for pair-2 of OTO dataset from German with names is",round(wpu2_oto_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu3_oto_n = (sum/240)
    print("Average sentiment score for pair-3 of OTO dataset from German with names is",round(wpu3_oto_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu4_oto_n = (sum/240)
    print("Average sentiment score for pair-3 of OTO dataset from German with names is",round(wpu4_oto_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu5_oto_n = (sum/240)
    print("Average sentiment score for pair-3 of OTO dataset from German with names is",round(wpu5_oto_n,2))

    return [wpu1_oto_n,wpu2_oto_n,wpu3_oto_n,wpu4_oto_n,wpu5_oto_n]

##Average sentiment scores for French dataset with names.
def calc_averages_de_n():

    pa = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu1_fr_n = (sum/240)
    print("Average sentiment score for pair-1 of German dataset with names is",round(wpu1_fr_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu2_fr_n = (sum/240)
    print("Average sentiment score for pair-2 of German dataset with names is",round(wpu2_fr_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu3_fr_n = (sum/240)
    print("Average sentiment score for pair-3 of German dataset with names is",round(wpu3_fr_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu4_fr_n = (sum/240)
    print("Average sentiment score for pair-3 of German dataset with names is",round(wpu4_fr_n,2))

    pa = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/textblob_de/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu5_fr_n = (sum/240)
    print("Average sentiment score for pair-3 of German dataset with names is",round(wpu5_fr_n,2))

    return [wpu1_fr_n,wpu2_fr_n,wpu3_fr_n,wpu4_fr_n,wpu5_fr_n]


##Average sentiment scores for Original English dataset with names.
def calc_averages_en_n():
    pa = pd.read_csv("../../data/results/textblob/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu1_en_n = (sum/240)
    print("Average sentiment score for pair-1 of original English dataset with names is",round(wpu1_en_n,2))

    pa = pd.read_csv("../../data/results/textblob/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu2_en_n = (sum/240)
    print("Average sentiment score for pair-2 of original English dataset with names is",round(wpu2_en_n,2))

    pa = pd.read_csv("../../data/results/textblob/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu3_en_n = (sum/240)
    print("Average sentiment score for pair-3 of original English dataset with namesis",round(wpu3_en_n,2))

    pa = pd.read_csv("../../data/results/textblob/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu4_en_n = (sum/240)
    print("Average sentiment score for pair-3 of original English dataset with namesis",round(wpu4_en_n,2))

    pa = pd.read_csv("../../data/results/textblob/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    pb = pd.read_csv("../../data/results/textblob/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    pc = pd.read_csv("../../data/results/textblob/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    sum = 0
    for each in pa['Sentiment']:
        sum = sum + each
    for each in pb['Sentiment']:
        sum = sum + each
    for each in pc['Sentiment']:
        sum = sum + each

    wpu5_en_n = (sum/240)
    print("Average sentiment score for pair-3 of original English dataset with names is",round(wpu5_en_n,2))

    return [wpu1_en_n,wpu2_en_n,wpu3_en_n,wpu4_en_n,wpu5_en_n]
