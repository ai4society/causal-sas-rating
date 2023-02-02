import pandas as pd
import os


"""
Different Race + Gender combinations
Race = 0, Gender = 0 --> Unknown gender and race
Race = 1, Gender = 1 --> European male
Race = 1, Gender = 2 --> Europen female
Race = 2, Gender = 1 --> Afro-American male
Race = 2, Gender = 2 --> Afro-American female

"""

def gen_rg(path,dest):

    data = pd.read_csv(path)

    rg = []
    for r,g in zip(data['Race'],data['Gender']):
        if r == 0 and g == 0:
            rg.append(0)
        elif r == 1 and g == 1:
            rg.append(1)
        elif r == 1 and g == 2:
            rg.append(2)
        elif r == 2 and g ==1:
            rg.append(3)
        elif r == 2 and g == 2:
            rg.append(4)

    data['RG'] = rg

    data.to_csv(dest, index=False)


p = "../../data/results/group3/"
for folder in os.listdir(p):
    for file in os.listdir(p + folder):
        print("Processing {}".format(folder))
        print("Processing {}\n".format(file))
        dest = '../../data/results/group3_combined/'+folder+'/'+'comb_'+file
        with open(os.path.join(p+folder+"/"+file), 'r') as f:
            gen_rg(f,dest)

print("Done!")

p = "../../data/results/group4/"
for folder in os.listdir(p):
    for file in os.listdir(p + folder):
        print("Processing {}".format(folder))
        print("Processing {}\n".format(file))
        dest = '../../data/results/group4_combined/'+folder+'/'+'comb_'+file
        with open(os.path.join(p+folder+"/"+file), 'r') as f:
            gen_rg(f,dest)

print("Done!")

p = "../../data/results/continuous/group3/"
for folder in os.listdir(p):
    for file in os.listdir(p + folder):
        print("Processing {}".format(folder))
        print("Processing {}\n".format(file))
        dest = '../../data/results/continuous/group3_combined/'+folder+'/'+'comb_'+file
        with open(os.path.join(p+folder+"/"+file), 'r') as f:
            gen_rg(f,dest)

print("Done!")

p = "../../data/results/continuous/group4/"
for folder in os.listdir(p):
    for file in os.listdir(p + folder):
        print("Processing {}".format(folder))
        print("Processing {}\n".format(file))
        dest = '../../data/results/continuous/group4_combined/'+folder+'/'+'comb_'+file
        with open(os.path.join(p+folder+"/"+file), 'r') as f:
            gen_rg(f,dest)

print("Done!")
