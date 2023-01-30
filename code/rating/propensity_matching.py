import pandas as pd
from causalinference import CausalModel


data = pd.read_csv('e3_gru.csv')
Y = data.loc[:,"Sentiment"].values
# Treatment
X = data.loc[:,"Emotion"].values
# Confounders
Z = data.drop(columns = ["Sentiment", "Emotion"]).values


print("Before estimating propensity score:\n\n")
model = CausalModel(Y,X,Z)
model.est_via_matching(bias_adj = True)
print(model.estimates)

print("After estimating propensity score:\n\n")
model = CausalModel(Y,X,Z)
print(model.summary_stats)
print(model.estimates)
model.est_propensity_s()
print(model.blocks)
print(model.propensity)
model.trim_s()
model.stratify_s()
print(model.strata)
model.est_via_matching(bias_adj = True)
print(model.estimates)

