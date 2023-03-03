import pandas as pd
from math import sqrt
import numpy as np
from numpy.random import seed
from numpy.random import randn
from numpy import mean
from scipy.stats import sem
from scipy.stats import t
import os

# Source: This function was taken from 'https://machinelearningmastery.com/how-to-code-the-students-t-test-from-scratch-in-python/'
def t_test(data1, data2):
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
	# calculate the p-value
	p = (1.0 - t.cdf(abs(t_stat), df)) * 2.0
	# return everything
	return t_stat, df, p


# calculate the critical value
def look_up(alpha,dof):
	crit = t.ppf(1-alpha/2,dof)

	return crit

# Calculate the weighted rejection score based on whether the null hypothesis is rejected or accepted.
def weighted_rejection_score(D, A, W, P):

	if (P == 'G'):
		psi = 0
		for alpha, w in zip(A, W):
			# print("Weight:", w)
			for d_o in D:
				with open(d_o, 'r') as f:
					d = pd.read_csv(d_o)
					d1 = d['Sentiment'][d['Gender'] == 0]
					d2 = d['Sentiment'][d['Gender'] == 1]
					t, dof, p = t_test(d1,d2)
					t_crit = look_up(alpha, dof)
					# print(t, t_crit)

					if abs(t) > t_crit:
						psi = psi + w

					d1 = d['Sentiment'][d['Gender'] == 1]
					d2 = d['Sentiment'][d['Gender'] == 2]
					t, dof, p = t_test(d1,d2)
					t_crit = look_up(alpha, dof)
					# print(t, t_crit)

					if abs(t) > t_crit:
						psi = psi + w

					d1 = d['Sentiment'][d['Gender'] == 0]
					d2 = d['Sentiment'][d['Gender'] == 2]
					t, dof, p = t_test(d1,d2)
					t_crit = look_up(alpha, dof)
					# print(t, t_crit)

					if abs(t) > t_crit:
						psi = psi + w
		# print(psi)
		return psi

	elif (P == 'R'):
			psi = 0
			for alpha, w in zip(A, W):
				# print("Weight:", w)
				for d_o in D:
					with open(d_o, 'r') as f:
						d = pd.read_csv(d_o)
						d1 = d['Sentiment'][d['Race'] == 0]
						d2 = d['Sentiment'][d['Race'] == 1]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['Race'] == 1]
						d2 = d['Sentiment'][d['Race'] == 2]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['Race'] == 0]
						d2 = d['Sentiment'][d['Race'] == 2]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

			return psi

	elif (P == 'RG'):
			psi = 0
			for alpha, w in zip(A, W):
				# print("Weight:", w)
				for d_o in D:
					with open(d_o, 'r') as f:
						d = pd.read_csv(d_o)
						d1 = d['Sentiment'][d['RG'] == 0]
						d2 = d['Sentiment'][d['RG'] == 1]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['RG'] == 0]
						d2 = d['Sentiment'][d['RG'] == 2]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['RG'] == 0]
						d2 = d['Sentiment'][d['RG'] == 3]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w


						d1 = d['Sentiment'][d['RG'] == 0]
						d2 = d['Sentiment'][d['RG'] == 4]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['RG'] == 1]
						d2 = d['Sentiment'][d['RG'] == 2]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w


						d1 = d['Sentiment'][d['RG'] == 1]
						d2 = d['Sentiment'][d['RG'] == 3]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w


						d1 = d['Sentiment'][d['RG'] == 1]
						d2 = d['Sentiment'][d['RG'] == 4]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w



						d1 = d['Sentiment'][d['RG'] == 2]
						d2 = d['Sentiment'][d['RG'] == 3]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['RG'] == 2]
						d2 = d['Sentiment'][d['RG'] == 4]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w

						d1 = d['Sentiment'][d['RG'] == 3]
						d2 = d['Sentiment'][d['RG'] == 4]
						t, dof, p = t_test(d1,d2)
						t_crit = look_up(alpha, dof)
						# print(t, t_crit)

						if abs(t) > t_crit:
							psi = psi + w
			return psi


# Creating a partial order using the weighted rejection score.
def create_partial_order(S,D,A,W,P):
	KV = {}
	for s,i in zip(S,range(0,25,5)):
		D_t = D[i:i+5]
		# print("SAS: ", s)
		# print(D_t)
		psi = weighted_rejection_score(D_t,A,W,P)
		KV[s] = psi
	# Source: Following line is taken from 'https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value'
	PO = dict(sorted(KV.items(), key=lambda item: item[1]))
	print(PO)

	return PO


# Assign final rating to each of the SASs based on the chosen number of rating levels and the partial order.
def assign_rating(S,D,A,W,L,P):
	R = {}

	PO = create_partial_order(S,D,A,W,P)
	V = list(PO.values())
	levels = np.array_split(V,L)
	levels = [list(each) for each in levels]

	t1 = []
	for k,i in zip(PO,PO.values()):
		for l in levels:
			if i in l:
				t1.append(l)
				# so that it could pick the 1st matched array.
				break

	t1 = [list(each) for each in t1]
	# print(t1)
	# print(levels)

	r = [levels.index(each)+1 for each in t1]


	for k, i in zip(PO,r):
		R[k] = i

	return R







# # Weights corresponding to different CIs
W = [1, 0.7, 0.6]
A = [0.025, 0.15, 0.2]

# Number of rating levels. For ex., L = 3 denotes three rating levels (1,2,3)
L = 3
S = []
D = []

# Group-1
path = "../../data/results/group1/"

for folder in os.listdir("../../data/results/group1/"):
	for file in os.listdir(path + folder):
		S.append(folder)
		D.append(os.path.join(path+folder+"/"+file))

S = sorted(list(set(S)))


print("The final rating based on the Group-1 results are: ")
print(assign_rating(S,D,A,W,L,'G'))
print("\n")

# Group-3
S = []
D = []
path = "../../data/results/group3/"

for folder in os.listdir("../../data/results/group3/"):
	for file in os.listdir(path + folder):
		S.append(folder)
		D.append(os.path.join(path+folder+"/"+file))

S = sorted(list(set(S)))

print("The final rating based on the Group-3 gender (names as proxy) results are: ")
print(assign_rating(S,D,A,W,L,'G'))
print("\n")



print("The final rating based on the Group-3 race (names as proxy) results are: ")
print(assign_rating(S,D,A,W,L,'R'))
print("\n")

# Group-3 (Composite case)
S = []
D = []
path = "../../data/results/group3_combined/"

for folder in os.listdir("../../data/results/group3_combined/"):
	for file in os.listdir(path + folder):
		S.append(folder)
		D.append(os.path.join(path+folder+"/"+file))

S = sorted(list(set(S)))

print("The final rating based on the Group-3 RG (gender and race combined) results are: ")
print(assign_rating(S,D,A,W,L,'RG'))
print("\n")


## Continuous Data Analysis

# Weights corresponding to different CIs
W = [1, 0.7, 0.6]
# For CIs: 95%, 70%, 60%.
A = [0.025, 0.15, 0.2]
# Number of rating levels. For ex., L = 3 denotes three rating levels (1,2,3)
L = 3
S = []
D = []

print("RESULTS FOR CONTINUOUS SENTIMENT VALUES: \n")
# Group-1
path = "../../data/results/continuous/group1/"

for folder in os.listdir("../../data/results/continuous/group1/"):
	for file in os.listdir(path + folder):
		S.append(folder)
		D.append(os.path.join(path+folder+"/"+file))

S = sorted(list(set(S)))


print("The final rating based on the Group-1 results are: ")
print(assign_rating(S,D,A,W,L,'G'))
print("\n")

# Group-3
S = []
D = []
path = "../../data/results/continuous/group3/"

for folder in os.listdir("../../data/results/continuous/group3/"):
	for file in os.listdir(path + folder):
		S.append(folder)
		D.append(os.path.join(path+folder+"/"+file))

S = sorted(list(set(S)))

print("The final rating based on the Group-3 gender (pronouns as proxy) results are: ")
print(assign_rating(S,D,A,W,L,'G'))
print("\n")



print("The final rating based on the Group-3 race (names as proxy) results are: ")
print(assign_rating(S,D,A,W,L,'R'))
print("\n")


# Group-3 Combined
S = []
D = []
path = "../../data/results/continuous/group3_combined/"

for folder in os.listdir("../../data/results/continuous/group3_combined/"):
	for file in os.listdir(path + folder):
		S.append(folder)
		D.append(os.path.join(path+folder+"/"+file))

S = sorted(list(set(S)))

print("The final rating based on the Group-3 combined results are: ")
print(assign_rating(S,D,A,W,L,'RG'))
print("\n")
