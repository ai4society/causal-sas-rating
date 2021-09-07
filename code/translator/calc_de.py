from tran_senti_avg_de import calc_averages_de_oto,calc_averages_de,calc_averages_en,\
                            calc_averages_de_oto_n,calc_averages_de_n,calc_averages_en_n

from tran_senti_diff_de import diff_withnames_de,diff_nonames_de


from word_diff_de import word_diff_nonames_de,word_diff_withnames_de
from gender_diff_de import gen_diff_withnames_de,gen_diff_nonames_de

import pandas as pd
import csv
import sys

from pandas import DataFrame
print("Please wait for few seconds")



stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/calculations_de.txt", "w")


#Calculating average sentiment scores for the TextBlob results without names.
def calc_avg_nonames():

    print("The average scores for OTO dataset from German without names are:")
    calc_averages_de_oto()
    print("\n")
    print("The average scores of German dataset without names are:")
    calc_averages_de()
    print("\n")
    print("The average scores of original English dataset without names are:")
    calc_averages_en()

    data = {'pairs':['p1','p2','p3','p4','p5'],'avg sentiment of OTO w/o names':calc_averages_de_oto()}
    df = pd.DataFrame.from_dict(data)
    df.to_csv('../../data/results/analysis/calculations_de.csv', mode='w')

    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment of German w/o names"] = calc_averages_de()
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment of English w/o names"] = calc_averages_en()
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

#Calculating average sentiment scores for the TextBlob results with names.
def calc_avg_withnames():

    print("\n")
    print("The average scores of OTO from German dataset with names are:")
    calc_averages_de_oto_n()
    print("\n")
    print("The average scores of German dataset with names are:")
    calc_averages_de_n()
    print("\n")
    print("The average scores of original English dataset with names are:")
    calc_averages_en_n()

    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment of OTO with names"] = calc_averages_de_oto_n()
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment of German with names"] = calc_averages_de_n()
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment of English with names"] = calc_averages_en_n()
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

#Calculating the % average difference sentiment score between OTO and original English dataset without names.
def calc_diff_nonames():
    sum = 0
    for each in diff_nonames_de()[0]:
        sum = sum + each
    for each in diff_nonames_de()[1]:
        sum = sum + each
    for each in diff_nonames_de()[2]:
        sum = sum + each

    p1_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames_de()[3]:
        sum = sum + each
    for each in diff_nonames_de()[4]:
        sum = sum + each
    for each in diff_nonames_de()[5]:
        sum = sum + each

    p2_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames_de()[6]:
        sum = sum + each
    for each in diff_nonames_de()[7]:
        sum = sum + each
    for each in diff_nonames_de()[8]:
        sum = sum + each

    p3_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames_de()[9]:
        sum = sum + each
    for each in diff_nonames_de()[10]:
        sum = sum + each
    for each in diff_nonames_de()[11]:
        sum = sum + each

    p4_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames_de()[12]:
        sum = sum + each
    for each in diff_nonames_de()[13]:
        sum = sum + each
    for each in diff_nonames_de()[14]:
        sum = sum + each

    p5_avg = (sum/240)*100


    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment difference without names (%)"] = [round(p1_avg,2),round(p2_avg,2),round(p3_avg,2),round(p4_avg,2),round(p5_avg,2)]
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)
    return (round(p1_avg,2),round(p2_avg,2),round(p3_avg,2),round(p4_avg,2),round(p5_avg,2))


#Calculating the % average difference sentiment score between OTO and original English dataset with names.
def calc_diff_withnames():
    sum = 0
    for each in diff_withnames_de()[0]:
        sum = sum + each
    for each in diff_withnames_de()[1]:
        sum = sum + each
    for each in diff_withnames_de()[2]:
        sum = sum + each

    p1_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames_de()[3]:
        sum = sum + each
    for each in diff_withnames_de()[4]:
        sum = sum + each
    for each in diff_withnames_de()[5]:
        sum = sum + each

    p2_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames_de()[6]:
        sum = sum + each
    for each in diff_withnames_de()[7]:
        sum = sum + each
    for each in diff_withnames_de()[8]:
        sum = sum + each

    p3_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames_de()[9]:
        sum = sum + each
    for each in diff_withnames_de()[10]:
        sum = sum + each
    for each in diff_withnames_de()[11]:
        sum = sum + each

    p4_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames_de()[12]:
        sum = sum + each
    for each in diff_withnames_de()[13]:
        sum = sum + each
    for each in diff_withnames_de()[14]:
        sum = sum + each

    p5_avg_n = (sum/240)*100

    df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
    df["avg sentiment difference with names (%)"] = [round(p1_avg_n,2),round(p2_avg_n,2),round(p3_avg_n,2),round(p4_avg_n,2),round(p5_avg_n,2)]
    df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)


    return (round(p1_avg_n,2),round(p2_avg_n,2),round(p3_avg_n,2),round(p4_avg_n,2),round(p5_avg_n,2))


calc_avg_nonames()
calc_avg_withnames()
print("\n")
print("Average sentiment difference % (without names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(calc_diff_nonames()[0],calc_diff_nonames()[1],\
                                                                                                calc_diff_nonames()[2],calc_diff_nonames()[3],calc_diff_nonames()[4]))
print("\n")
print("Average sentiment difference % (with names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(calc_diff_withnames()[0],calc_diff_withnames()[1],\
                                                                                                calc_diff_withnames()[2],calc_diff_withnames()[3],calc_diff_withnames()[4]))

print("\n")



sys.stdout.close()
sys.stdout=stdoutOrigin

print("You can see the statistics in 'calculations_de.txt' file")



#####################################################################
# print("Please wait for few seconds to get word difference statistics")

stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/word_diff_nonames_de.txt", "w")

print("\n")
print("Average word difference % (without names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(word_diff_nonames_de()[0],word_diff_nonames_de()[1],word_diff_nonames_de()[2],word_diff_nonames_de()[3],word_diff_nonames_de()[4]))

sys.stdout.close()
sys.stdout=stdoutOrigin

df = pd.read_csv("../../data/results/analysis/calculations_de.csv")



df["Word difference without names (%)"] = word_diff_nonames_de()
df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

print("You can see the word differences (nonames) in 'word_diff_nonames_de.txt' file")



###################################################################


print("Please wait for few seconds to get word difference statistics")

stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/word_diff_withnames_de.txt", "w")

print("\n")
print("Average word difference % (with names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(word_diff_withnames_de()[0],word_diff_withnames_de()[1],word_diff_withnames_de()[2],word_diff_withnames_de()[3],word_diff_withnames_de()[4]))

sys.stdout.close()
sys.stdout=stdoutOrigin

df = pd.read_csv("../../data/results/analysis/calculations_de.csv")
df["Word difference with names (%)"] = word_diff_withnames_de()
df.to_csv("../../data/results/analysis/calculations_de.csv", index=False)

print("You can see the word differences (withnames) in 'word_diff_withnames_de.txt' file")

####################################################################

stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/gender_diff_nonames_de.txt", "w")

gen_diff_nonames_de()

sys.stdout.close()
sys.stdout=stdoutOrigin

print("You can see difference in gender variables at 'gender_diff_nonames_de.txt'")
#
# ####################################################################
stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/gender_diff_withnames_de.txt", "w")

gen_diff_withnames_de()

sys.stdout.close()
sys.stdout=stdoutOrigin
print("You can see difference in gender variables at 'gender_diff_withnames_de.txt'")
