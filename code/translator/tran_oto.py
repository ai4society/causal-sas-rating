import google_trans_new
from google_trans_new import google_translator
import pandas as pd

import tran
from tran import tran_oto,tran_oto_names


for i in range(1,6):
    print("Generating OTO dataset from French {}/5 without names".format(i))
    tran_oto("../../data/data-generated/nonames_french/bf{}_fr.csv".format(i),"bf{}".format(i))
    tran_oto("../../data/data-generated/nonames_french/bm{}_fr.csv".format(i),"bm{}".format(i))
    tran_oto("../../data/data-generated/nonames_french/u{}_fr.csv".format(i),"u{}".format(i))

for i in range(1,6):
    print("Generating OTO dataset from French {}/5 with names".format(i))
    tran_oto_names("../../data/data-generated/withnames_french/bf{}_fr.csv".format(i),"bf{}".format(i))
    tran_oto_names("../../data/data-generated/withnames_french/bm{}_fr.csv".format(i),"bm{}".format(i))
    tran_oto_names("../../data/data-generated/withnames_french/u{}_fr.csv".format(i),"u{}".format(i))
