import google_trans_new
from google_trans_new import google_translator
import pandas as pd

import tran
from tran import tran_oto_german,tran_oto_names_german


for i in range(1,6):
    print("Generating OTO dataset from German {}/5 without names".format(i))
    tran_oto_german("../../data/data-generated/nonames_de/bf{}_de.csv".format(i),"bf{}".format(i))
    tran_oto_german("../../data/data-generated/nonames_de/bm{}_de.csv".format(i),"bm{}".format(i))
    tran_oto_german("../../data/data-generated/nonames_de/u{}_de.csv".format(i),"u{}".format(i))

for i in range(1,6):
    print("Generating OTO dataset from German {}/5 with names".format(i))
    tran_oto_names_german("../../data/data-generated/withnames_de/bf{}_de.csv".format(i),"bf{}".format(i))
    tran_oto_names_german("../../data/data-generated/withnames_de/bm{}_de.csv".format(i),"bm{}".format(i))
    tran_oto_names_german("../../data/data-generated/withnames_de/u{}_de.csv".format(i),"u{}".format(i))
