import pandas as pd



def word_diff1(s1,s2):
    xy = set(s1.lower().split()) - set(s2.lower().split())
    yx =  set(s2.lower().split()) - set(s1.lower().split())
    den = len(s1.split()) + len(s2.split())
    return xy.union(yx),den




##Calculating the difference between words of original english dataset and French to OTO dataset with names.
def word_diff_withnames_de():

    #For 1st pair of words
    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p1_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p1_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])




    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p1_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p1_avg_wd = (sum/240)*100

    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p2_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p2_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])




    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p2_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p2_avg_wd = (sum/240)*100



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p3_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p3_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p3_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p3_avg_wd = (sum/240)*100

    """"""

    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p4_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p4_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p4_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    p4_avg_wd = (sum/240)*100

    """"""
    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p5_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p5_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])




    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/withnames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p5_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    p5_avg_wd = (sum/240)*100

    return [round(p1_avg_wd,2),round(p2_avg_wd,2),round(p3_avg_wd,2),round(p4_avg_wd,2),round(p5_avg_wd,2)]

#
#
#
# ##Word differences between original English dataset and OTO dataset without names.
def word_diff_nonames_de():

    #For 1st pair of words
    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p1_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p1_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p1_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p1_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])




    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p1_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p1_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p1_avg_wd = (sum/240)*100

    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p2_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p2_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p2_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p2_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p2_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p2_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p2_avg_wd = (sum/240)*100



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p3_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p3_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p3_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p3_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])




    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p3_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p3_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p3_avg_wd = (sum/240)*100

    """"""

    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p4_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p4_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p4_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p4_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p4_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p4_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p4_avg_wd = (sum/240)*100

    """"""
    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p5_b_.1_.9.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p5_b1 are: ")
    # print("\n")
    sum = 0
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])


    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p5_b_.9_.1.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p5_b2 are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])



    d1 = pd.read_csv("../../data/results/textblob/textblob_de_oto/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")
    d2 = pd.read_csv("../../data/results/textblob/nonames/result_p5_u_.5_.5.csv",engine="python",encoding="latin-1")

    # print("\n")
    # print("Word differences in p5_u are: ")
    # print("\n")
    for a,b in zip(d1['Sentence'],d2['Sentence']):
        #print(word_diff1(a.lower(),b.lower()),len(word_diff1(a.lower(),b.lower())))
        sum = sum + (len(word_diff1(a.lower(),b.lower())[0])/word_diff1(a.lower(),b.lower())[1])

    p5_avg_wd = (sum/240)*100

    return [round(p1_avg_wd,2),round(p2_avg_wd,2),round(p3_avg_wd,2),round(p4_avg_wd,2),round(p5_avg_wd,2)]
