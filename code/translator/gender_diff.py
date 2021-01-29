import pandas as pd

def gen_diff_nonames():
    original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

    male = list(sorted(set(original_data[original_data['Gender']=='male']['Person'])))[-10:]
    male[0] = male[0].replace("him","my nephew")

    female = list(sorted(set(original_data[original_data['Gender']=='female']['Person'])))[-10:]
    female[7] = female[7].replace("she","my niece")



    male = [each.replace("my ","") for each in male]
    male = [each.replace("this ","") for each in male]
    #print(male)

    female = [each.replace("my ","") for each in female]
    female = [each.replace("this ","") for each in female]
    #print(female)

    print("\n")
    print("For biased female datasets: ")
    for i in range(1,6):
        d1 = pd.read_csv("../../data/data-generated/nonames/bf{}.csv".format(i),engine="python",encoding="latin-1")
        d2 = pd.read_csv("../../data/data-generated/nonames_fr_oto/bf{}_fr_oto.csv".format(i),engine="python",encoding="latin-1")

        for x,y in zip(d1['Sentences'],d2[' Phrases']):
            d1_m = set(x.lower().split()) & set(male)
            d1_f = set(x.lower().split()) & set(female)
            d2_m = set(y.lower().split()) & set(male)
            d2_f = set(y.lower().split()) & set(female)

            #print("The changed gender variables for are:")
            if ((list(d1_m) == list(d2_m)) == False):
                if(d2_m):
                    print(d1_m,d2_m)
                else:
                    print(x,y)
            if ((list(d1_f) == list(d2_f)) == False):
                if(d2_f):
                    print(d1_f,d2_f)
                else:
                    print(x,y)

    print("\n")
    print("For biased male datasets: ")
    for i in range(1,6):
        d1 = pd.read_csv("../../data/data-generated/nonames/bm{}.csv".format(i),engine="python",encoding="latin-1")
        d2 = pd.read_csv("../../data/data-generated/nonames_fr_oto/bm{}_fr_oto.csv".format(i),engine="python",encoding="latin-1")

        for x,y in zip(d1['Sentences'],d2[' Phrases']):
            d1_m = set(x.lower().split()) & set(male)
            d1_f = set(x.lower().split()) & set(female)
            d2_m = set(y.lower().split()) & set(male)
            d2_f = set(y.lower().split()) & set(female)

            if ((list(d1_m) == list(d2_m)) == False):
                if(d2_m):
                    print(d1_m,d2_m)
                else:
                    print(x,y)
            if ((list(d1_f) == list(d2_f)) == False):
                if(d2_f):
                    print(d1_f,d2_f)
                else:
                    print(x,y)

    print("\n")
    print("For unbiased datasets: ")
    for i in range(1,6):
        d1 = pd.read_csv("../../data/data-generated/nonames/u{}.csv".format(i),engine="python",encoding="latin-1")
        d2 = pd.read_csv("../../data/data-generated/nonames_fr_oto/u{}_fr_oto.csv".format(i),engine="python",encoding="latin-1")

        for x,y in zip(d1['Sentences'],d2[' Phrases']):
            d1_m = set(x.lower().split()) & set(male)
            d1_f = set(x.lower().split()) & set(female)
            d2_m = set(y.lower().split()) & set(male)
            d2_f = set(y.lower().split()) & set(female)

            if ((list(d1_m) == list(d2_m)) == False):
                if(d2_m):
                    print(d1_m,d2_m)
                else:
                    print(x,y)
            if ((list(d1_f) == list(d2_f)) == False):
                if(d2_f):
                    print(d1_f,d2_f)
                else:
                    print(x,y)

def gen_diff_withnames():

    original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

    male = list(sorted(set(original_data[original_data['Gender']=='male']['Person'])))[:10]
    #print(male)
    female = list(sorted(set(original_data[original_data['Gender']=='female']['Person'])))[:10]
    #print(female)




    print("\n")
    print("For biased female datasets: ")
    for i in range(1,6):
        d1 = pd.read_csv("../../data/data-generated/withnames/bf{}.csv".format(i),engine="python",encoding="latin-1")
        d2 = pd.read_csv("../../data/data-generated/withnames_fr_oto/bf{}_fr_oto.csv".format(i),engine="python",encoding="latin-1")

        for x,y in zip(d1['Sentences'],d2[' Phrases']):
            d1_m = set(x.lower().split()) & set(male)
            d1_f = set(x.lower().split()) & set(female)
            d2_m = set(y.lower().split()) & set(male)
            d2_f = set(y.lower().split()) & set(female)

            #print("The changed gender variables for are:")
            if ((list(d1_m) == list(d2_m)) == False):
                print(d1_m,d2_m)
            if ((list(d1_f) == list(d2_f)) == False):
                print(d1_f,d2_f)

    print("\n")
    print("For biased male datasets: ")
    for i in range(1,6):
        d1 = pd.read_csv("../../data/data-generated/withnames/bm{}.csv".format(i),engine="python",encoding="latin-1")
        d2 = pd.read_csv("../../data/data-generated/withnames_fr_oto/bm{}_fr_oto.csv".format(i),engine="python",encoding="latin-1")

        for x,y in zip(d1['Sentences'],d2[' Phrases']):
            d1_m = set(x.lower().split()) & set(male)
            d1_f = set(x.lower().split()) & set(female)
            d2_m = set(y.lower().split()) & set(male)
            d2_f = set(y.lower().split()) & set(female)

            if ((list(d1_m) == list(d2_m)) == False):
                print(d1_m,d2_m)
            if ((list(d1_f) == list(d2_f)) == False):
                print(d1_f,d2_f)

    print("\n")
    print("For unbiased datasets: ")
    for i in range(1,6):
        d1 = pd.read_csv("../../data/data-generated/withnames/u{}.csv".format(i),engine="python",encoding="latin-1")
        d2 = pd.read_csv("../../data/data-generated/withnames_fr_oto/u{}_fr_oto.csv".format(i),engine="python",encoding="latin-1")

        for x,y in zip(d1['Sentences'],d2[' Phrases']):
            d1_m = set(x.lower().split()) & set(male)
            d1_f = set(x.lower().split()) & set(female)
            d2_m = set(y.lower().split()) & set(male)
            d2_f = set(y.lower().split()) & set(female)

            if ((list(d1_m) == list(d2_m)) == False):
                print(d1_m,d2_m)
            if ((list(d1_f) == list(d2_f)) == False):
                print(d1_f,d2_f)
