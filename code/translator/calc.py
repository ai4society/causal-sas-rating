from tran_senti_avg import calc_averages_fr_oto,calc_averages_fr,calc_averages_en,\
                            calc_averages_fr_oto_n,calc_averages_fr_n,calc_averages_en_n

from tran_senti_diff import diff_withnames,diff_nonames

from word_diff import word_diff_nonames,word_diff_withnames

from gender_diff import gen_diff_withnames,gen_diff_nonames

import pandas as pd

import sys


print("Please wait for few seconds")

stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/calculations.txt", "w")


#Calculating average sentiment scores for the TextBlob results without names.
def calc_avg_nonames():

    print("The average scores for OTO dataset from French without names are:")
    calc_averages_fr_oto()
    print("\n")
    print("The average scores of French dataset without names are:")
    calc_averages_fr()
    print("\n")
    print("The average scores of original English dataset without names are:")
    calc_averages_en()

#Calculating average sentiment scores for the TextBlob results with names.
def calc_avg_withnames():

    print("\n")
    print("The average scores of OTO from French dataset with names are:")
    calc_averages_fr_oto_n()
    print("\n")
    print("The average scores of French dataset with names are:")
    calc_averages_fr_n()
    print("\n")
    print("The average scores of original English dataset with names are:")
    calc_averages_en_n()




#Calculating the % average difference sentiment score between OTO and original English dataset without names.
def calc_diff_nonames():
    sum = 0
    for each in diff_nonames()[0]:
        sum = sum + each
    for each in diff_nonames()[1]:
        sum = sum + each
    for each in diff_nonames()[2]:
        sum = sum + each

    p1_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames()[3]:
        sum = sum + each
    for each in diff_nonames()[4]:
        sum = sum + each
    for each in diff_nonames()[5]:
        sum = sum + each

    p2_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames()[6]:
        sum = sum + each
    for each in diff_nonames()[7]:
        sum = sum + each
    for each in diff_nonames()[8]:
        sum = sum + each

    p3_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames()[9]:
        sum = sum + each
    for each in diff_nonames()[10]:
        sum = sum + each
    for each in diff_nonames()[11]:
        sum = sum + each

    p4_avg = (sum/240)*100

    sum = 0
    for each in diff_nonames()[12]:
        sum = sum + each
    for each in diff_nonames()[13]:
        sum = sum + each
    for each in diff_nonames()[14]:
        sum = sum + each

    p5_avg = (sum/240)*100

    return (round(p1_avg,2),round(p2_avg,2),round(p3_avg,2),round(p4_avg,2),round(p5_avg,2))


#Calculating the % average difference sentiment score between OTO and original English dataset with names.
def calc_diff_withnames():
    sum = 0
    for each in diff_withnames()[0]:
        sum = sum + each
    for each in diff_withnames()[1]:
        sum = sum + each
    for each in diff_withnames()[2]:
        sum = sum + each

    p1_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames()[3]:
        sum = sum + each
    for each in diff_withnames()[4]:
        sum = sum + each
    for each in diff_withnames()[5]:
        sum = sum + each

    p2_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames()[6]:
        sum = sum + each
    for each in diff_withnames()[7]:
        sum = sum + each
    for each in diff_withnames()[8]:
        sum = sum + each

    p3_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames()[9]:
        sum = sum + each
    for each in diff_withnames()[10]:
        sum = sum + each
    for each in diff_withnames()[11]:
        sum = sum + each

    p4_avg_n = (sum/240)*100

    sum = 0
    for each in diff_withnames()[12]:
        sum = sum + each
    for each in diff_withnames()[13]:
        sum = sum + each
    for each in diff_withnames()[14]:
        sum = sum + each

    p5_avg_n = (sum/240)*100

    return (round(p1_avg_n,2),round(p2_avg_n,2),round(p3_avg_n,2),round(p4_avg_n,2),round(p5_avg_n,2))



print("\n")
print("Average sentiment difference % (without names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(calc_diff_nonames()[0],calc_diff_nonames()[1],\
                                                                                                calc_diff_nonames()[2],calc_diff_nonames()[3],calc_diff_nonames()[4]))
print("\n")
print("Average sentiment difference % (with names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(calc_diff_withnames()[0],calc_diff_withnames()[1],\
                                                                                                calc_diff_withnames()[2],calc_diff_withnames()[3],calc_diff_withnames()[4]))

print("\n")

calc_avg_nonames()
calc_avg_withnames()

sys.stdout.close()
sys.stdout=stdoutOrigin

print("You can see the statistics in 'calculations.txt' file")

###################################################################

#
# print("Please wait for few seconds to get word difference statistics")

stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/word_diff_withnames.txt", "w")

print("\n")
print("Average word difference % (with names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(word_diff_withnames()[0],word_diff_withnames()[1],word_diff_withnames()[2],word_diff_withnames()[3],word_diff_withnames()[4]))

sys.stdout.close()
sys.stdout=stdoutOrigin

print("You can see the word differences (withnames) in 'word_diff_withnames.txt' file")



####################################################################

# print("Please wait for few seconds to get word difference statistics")

stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/word_diff_nonames.txt", "w")

print("\n")
print("Average word difference % (without names) for p1 is {},\np2 is {},\np3 is {},\np4 is {},\nand p5 is {}".format(word_diff_nonames()[0],word_diff_nonames()[1],word_diff_nonames()[2],word_diff_nonames()[3],word_diff_nonames()[4]))

sys.stdout.close()
sys.stdout=stdoutOrigin

print("You can see the word differences (nonames) in 'word_diff_nonames.txt' file")


#####################################################################
stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/gender_diff_nonames.txt", "w")

gen_diff_nonames()

sys.stdout.close()
sys.stdout=stdoutOrigin

print("You can see difference in gender variables at 'gender_diff_nonames.txt'")

####################################################################
stdoutOrigin=sys.stdout
sys.stdout = open("../../data/results/analysis/gender_diff_withnames.txt", "w")

gen_diff_withnames()

sys.stdout.close()
sys.stdout=stdoutOrigin
print("You can see difference in gender variables at 'gender_diff_withnames.txt'")
