import pandas as pd
from pandas import DataFrame

##Calculating the difference between scores of original english dataset and French to OTO dataset without names.
def diff_nonames():

    #For 1st pair of words
    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p1b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p1b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p1u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001))for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p2b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p2b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p2u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]



    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p3b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p3b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p3u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    """"""

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p4b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p4b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p4u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    """"""
    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p5b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p5b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p5u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]



    return [d_p1b1,d_p1b2,d_p1u1,d_p2b1,d_p2b2,d_p2u1,d_p3b1,d_p3b2,d_p3u1,d_p4b1,d_p4b2,d_p4u1,d_p5b1,d_p5b2,d_p5u1]


##Calculating the difference between scores of original english dataset and French to OTO dataset with names.
def diff_withnames():

    #For 1st pair of words
    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p1b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p1b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p1u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001))for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p2b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p2b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p2u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]



    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p3b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p3b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p3u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    """"""

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p4b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p4b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p4u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    """"""
    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p5b1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p5b2 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]


    d1 = pd.read_csv("../../data/results/textblob/textblob_fr_oto/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")


    a = []
    b = []
    for each in d1['Sentiment']:
        a.append(each)

    for each in d2['Sentiment']:
        b.append(each)

    d_p5u1 = [(((y+1.0001) - (x+1.0001)) / (x+1.0001)) for x,y in zip(a,b)]

    return [d_p1b1,d_p1b2,d_p1u1,d_p2b1,d_p2b2,d_p2u1,d_p3b1,d_p3b2,d_p3u1,d_p4b1,d_p4b2,d_p4u1,d_p5b1,d_p5b2,d_p5u1]
