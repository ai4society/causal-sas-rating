import pandas as pd
import researchpy as rp
import scipy.stats as stats
from scipy.stats import ttest_ind
import os
import sys
import numpy
import scipy
from math import sqrt
from numpy import mean
from scipy.stats import sem
from scipy.stats import t

# Source: This function was taken from 'https://machinelearningmastery.com/how-to-code-the-students-t-test-from-scratch-in-python/'
def t_test_calc(data1, data2, alpha):
	# calculate means
	mean1, mean2 = mean(data1), mean(data2)
	# calculate standard errors
	se1, se2 = sem(data1), sem(data2)
	# standard error on the difference between the samples
	sed = sqrt(se1**2.0 + se2**2.0)+ 0.0001
	# calculate the t statistic
	t_stat = (mean1 - mean2) / sed
	# degrees of freedom
	df = len(data1) + len(data2) - 2
	# calculate the critical value
	cv = t.ppf(1.0 - alpha/2, df)
	# calculate the p-value
	p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
	# return everything
	return t_stat, df, cv, p

def t_test_gender(path,alpha):

    df = pd.read_csv(path)

    s_final = []
    for s in df['Sentiment']:
        s_final.append(s+1)

    df['Sentiment'] = s_final

    d1 = df['Sentiment'][df['Gender'] == 0]
    d2 = df['Sentiment'][df['Gender'] == 1]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)
    print("For M,N: \n")
    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')

    print("\n t-value is: ")
    print(t)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")



    d1 = df['Sentiment'][df['Gender'] == 1]
    d2 = df['Sentiment'][df['Gender'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For M,F: \n")
    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")

    d1 = df['Sentiment'][df['Gender'] == 0]
    d2 = df['Sentiment'][df['Gender'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For N,F: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")


def t_test_race(path,alpha):

    df = pd.read_csv(path)

    s_final = []
    for s in df['Sentiment']:
        s_final.append(s+1)

    df['Sentiment'] = s_final

    d1 = df['Sentiment'][df['Race'] == 0]
    d2 = df['Sentiment'][df['Race'] == 1]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For E,N: \n")
    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")


    d1 = df['Sentiment'][df['Race'] == 1]
    d2 = df['Sentiment'][df['Race'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For E,A: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")


    d1 = df['Sentiment'][df['Race'] == 0]
    d2 = df['Sentiment'][df['Race'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For N,A: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")



def t_test_rg(path,alpha):

    df = pd.read_csv(path)

    s_final = []
    for s in df['Sentiment']:
        s_final.append(s+1)

    df['Sentiment'] = s_final

    d1 = df['Sentiment'][df['RG'] == 0]
    d2 = df['Sentiment'][df['RG'] == 1]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For UEM: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")



    d1 = df['Sentiment'][df['RG'] == 0]
    d2 = df['Sentiment'][df['RG'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For UEF: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")


    d1 = df['Sentiment'][df['RG'] == 0]
    d2 = df['Sentiment'][df['RG'] == 3]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For UAM: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 0]
    d2 = df['Sentiment'][df['RG'] == 4]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For UAF: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 1]
    d2 = df['Sentiment'][df['RG'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)


    print("For EMEF: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 1]
    d2 = df['Sentiment'][df['RG'] == 3]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For EMAM: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 1]
    d2 = df['Sentiment'][df['RG'] == 4]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)


    print("For EMAF: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 2]
    d2 = df['Sentiment'][df['RG'] == 3]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For EFAM: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 2]
    d2 = df['Sentiment'][df['RG'] == 4]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For EFAF: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print(t, p, dof)
    print("\n")

    d1 = df['Sentiment'][df['RG'] == 3]
    d2 = df['Sentiment'][df['RG'] == 4]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For AMAF: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')



    print(t, p, dof)
    print("\n")


# Two-tail t-test value

# CI = 95 %; alpha = 0.05
# CI = 70 %; alpha = 0.30
# CI = 60 %; alpha = 0.40
# Take one-tail t-test value.

alphas = [0.20, 0.15, 0.025]
f_names = ['60CI','70CI','95CI']


for alpha,name in zip(alphas,f_names):
    sys.stdout=open("calc_results/{}/group1_test_{}.txt".format(name,alpha),"w")

    print("\nFor Group 1: \n")
    path = "../../data/results/group1/"
    for folder in os.listdir("../../data/results/group1/"):
        for file in os.listdir(path + folder):
            # print(file, folder)
            print("Processing {}".format(folder))
            print("Calculating results for {}".format(file))
            with open(os.path.join(path+folder+"/"+file), 'r') as f:
                t_test_gender(f,alpha)

    sys.stdout.close()

    sys.stdout=open("calc_results/{}/group3_test_gender_{}.txt".format(name,alpha),"w")

    print("\nFor Group 3 gender: \n")
    path = "../../data/results/group3/"
    for folder in os.listdir("../../data/results/group3/"):
        for file in os.listdir(path + folder):
            # print(file, folder)
            print("Processing {}".format(folder))
            print("Calculating results for {}".format(file))
            with open(os.path.join(path+folder+"/"+file), 'r') as f:
                t_test_gender(f,alpha)

    sys.stdout.close()

    sys.stdout=open("calc_results/{}/group3_test_race_{}.txt".format(name,alpha),"w")

    print("\nFor Group 3 race: \n")
    path = "../../data/results/group3/"
    for folder in os.listdir("../../data/results/group3/"):
        for file in os.listdir(path + folder):
            # print(file, folder)
            print("Processing {}".format(folder))
            print("Calculating results for {}".format(file))
            with open(os.path.join(path+folder+"/"+file), 'r') as f:
                t_test_race(f,alpha)

    sys.stdout.close()


    sys.stdout=open("calc_results/{}/group3_comb_{}.txt".format(name,alpha),"w")


    print("\nFor Group 3 Combined: \n")
    path = "../../data/results/group3_combined/"
    for folder in os.listdir("../../data/results/group3_combined/"):
        for file in os.listdir(path + folder):
            # print(file, folder)
            print("Processing {}".format(folder))
            print("Calculating results for {}".format(file))
            with open(os.path.join(path+folder+"/"+file), 'r') as f:
                t_test_rg(f,alpha)

    sys.stdout.close()

for alpha,name in zip(alphas,f_names):

	sys.stdout=open("calc_results/continuous/{}/group1_test_{}.txt".format(name,alpha),"w")

	print("RESULTS FOR CONTINUOUS SENTIMENT VALUES: \n")

	print("\nFor Group 1: \n")

	# Group-1
	path = "../../data/results/continuous/group1/"

	for folder in os.listdir("../../data/results/continuous/group1/"):
		for file in os.listdir(path + folder):
			print("Processing {}".format(folder))
			print("Calculating results for {}".format(file))
			with open(os.path.join(path+folder+"/"+file), 'r') as f:
				t_test_gender(f,alpha)
	sys.stdout.close()


	# Group-3
	sys.stdout=open("calc_results/continuous/{}/group3_test_{}.txt".format(name,alpha),"w")
	print("\nFor Group 3 gender: \n")

	path = "../../data/results/continuous/group3/"

	for folder in os.listdir("../../data/results/continuous/group3/"):
		for file in os.listdir(path + folder):
			print("Processing {}".format(folder))
			print("Calculating results for {}".format(file))
			with open(os.path.join(path+folder+"/"+file), 'r') as f:
				t_test_gender(f,alpha)


	print("\nFor Group 3 race: \n")

	path = "../../data/results/continuous/group3/"

	for folder in os.listdir("../../data/results/continuous/group3/"):
		for file in os.listdir(path + folder):
			print("Processing {}".format(folder))
			print("Calculating results for {}".format(file))
			with open(os.path.join(path+folder+"/"+file), 'r') as f:
				t_test_race(f,alpha)

	sys.stdout.close()
	sys.stdout=open("calc_results/continuous/{}/group3_comb_{}.txt".format(name,alpha),"w")

	print("\nFor Group 3 Combined: \n")
	path = "../../data/results/continuous/group3_combined/"

	for folder in os.listdir("../../data/results/group3_combined/"):
		for file in os.listdir(path + folder):
			print("Processing {}".format(folder))
			print("Calculating results for {}".format(file))
			with open(os.path.join(path+folder+"/"+file), 'r') as f:
				t_test_rg(f,alpha)

	sys.stdout.close()
