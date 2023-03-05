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

def t_test_gender(path, alpha, ub):

    df = pd.read_csv(path)
    df = df[df['UB'] == ub]

    s_final = []
    for s in df['Sentiment']:
        s_final.append(s+1)

    df['Sentiment'] = s_final


    d1 = df['Sentiment'][df['User_gender'] == 0]
    d2 = df['Sentiment'][df['User_gender'] == 1]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)
    print("For M,N: \n")
    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')

    print("\n t-value is: ")
    print(t)
    print("\n")
    print("\n The t-crit value is: ")
    print(cv)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")




    d1 = df['Sentiment'][df['User_gender'] == 1]
    d2 = df['Sentiment'][df['User_gender'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For M,F: \n")
    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n The t-crit value is: ")
    print(cv)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")


    d1 = df['Sentiment'][df['User_gender'] == 0]
    d2 = df['Sentiment'][df['User_gender'] == 2]


    t, dof, cv, p = t_test_calc(d1,d2,alpha)

    print("For N,F: \n")

    if abs(t) <= cv:
        print('Accept null hypothesis that the means are equal.')
    else:
        print('Reject the null hypothesis that the means are equal.')


    print("\n t-value is: \n")
    print(t)
    print("\n")
    print("\n The t-crit value is: ")
    print(cv)
    print("\n")
    print("\n p-value is: ")
    print(p)
    print("\n")
    print("\n The DOF are: ")
    print(dof)
    print("\n")
    
    
    
    
alphas = [0.20, 0.15, 0.025]
f_names = ['60CI','70CI','95CI']

# User-side fairness
for alpha,name in zip(alphas,f_names):
    sys.stdout=open("calc_results/real-world/allure/{}/data_{}_user.txt".format(name,alpha),"w")

    path = "../../data/results/real-world/allure/"
    for folder in os.listdir(path):
        if folder.endswith('.DS_Store'):
            pass
        else:
            for file in os.listdir(path + folder):
                # print(file, folder)
                print("Processing {}".format(folder))
                print("Calculating results for {}".format(file))
                with open(os.path.join(path+folder+"/"+file), 'r') as f:
                    t_test_gender(f,alpha,1)

    sys.stdout.close()

# FOR ALLURE DATA:

# Bot-side fairness
for alpha,name in zip(alphas,f_names):
    sys.stdout=open("calc_results/real-world/allure/{}/data_{}_bot.txt".format(name,alpha),"w")

    path = "../../data/results/real-world/allure/"
    for folder in os.listdir(path):
        if folder.endswith('.DS_Store'):
            pass
        else:
            for file in os.listdir(path + folder):
                # print(file, folder)
                print("Processing {}".format(folder))
                print("Calculating results for {}".format(file))
                with open(os.path.join(path+folder+"/"+file), 'r') as f:
                    t_test_gender(f,alpha,0)

    sys.stdout.close()

# User-side fairness
for alpha,name in zip(alphas,f_names):
    sys.stdout=open("calc_results/real-world/allure/{}/data_{}_user.txt".format(name,alpha),"w")

    path = "../../data/results/real-world/allure/"
    for folder in os.listdir(path):
        if folder.endswith('.DS_Store'):
            pass
        else:
            for file in os.listdir(path + folder):
                # print(file, folder)
                print("Processing {}".format(folder))
                print("Calculating results for {}".format(file))
                with open(os.path.join(path+folder+"/"+file), 'r') as f:
                    t_test_gender(f,alpha,1)

    sys.stdout.close()


# FOR UNIBOT DATA:

# Bot-side fairness
for alpha,name in zip(alphas,f_names):
    sys.stdout=open("calc_results/real-world/unibot/{}/data_{}_bot.txt".format(name,alpha),"w")

    path = "../../data/results/real-world/unibot/"
    for folder in os.listdir(path):
        if folder.endswith('.DS_Store'):
            pass
        else:
            for file in os.listdir(path + folder):
                # print(file, folder)
                print("Processing {}".format(folder))
                print("Calculating results for {}".format(file))
                with open(os.path.join(path+folder+"/"+file), 'r') as f:
                    t_test_gender(f,alpha,0)

    sys.stdout.close()

    for alpha,name in zip(alphas,f_names):
        sys.stdout=open("calc_results/real-world/unibot/{}/data_{}_user.txt".format(name,alpha),"w")

        path = "../../data/results/real-world/unibot/"
        for folder in os.listdir(path):
            if folder.endswith('.DS_Store'):
                pass
            else:
                for file in os.listdir(path + folder):
                    # print(file, folder)
                    print("Processing {}".format(folder))
                    print("Calculating results for {}".format(file))
                    with open(os.path.join(path+folder+"/"+file), 'r') as f:
                        t_test_gender(f,alpha,1)

        sys.stdout.close()
