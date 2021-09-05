import tran
from tran import tran_french,tran_french_names
import edit_files


#Without names
for i in range(1,6):
    print("Generating French dataset {}/5 without names".format(i))
    tran_french("../../data/data-generated/nonames/bf{}.csv".format(i),"bf{}".format(i))
    tran_french("../../data/data-generated/nonames/bm{}.csv".format(i),"bm{}".format(i))
    tran_french("../../data/data-generated/nonames/u{}.csv".format(i),"u{}".format(i))

#With names.
for i in range(1,6):
    print("Generating French dataset {}/5 with names".format(i))
    tran_french_names("../../data/data-generated/withnames/bf{}.csv".format(i),"bf{}".format(i))
    tran_french_names("../../data/data-generated/withnames/bm{}.csv".format(i),"bm{}".format(i))
    tran_french_names("../../data/data-generated/withnames/u{}.csv".format(i),"u{}".format(i))

#Appending gender without names
print("Changing gender names from French to English")
for i in range(1,6):
    edit_files.edit_gender_french("../../data/data-generated/nonames_fr/bf{}_fr.csv".format(i),"../../data/data-generated/nonames/bf{}.csv".format(i),"bf{}".format(i))
    edit_files.edit_gender_french("../../data/data-generated/nonames_fr/bm{}_fr.csv".format(i),"../../data/data-generated/nonames/bm{}.csv".format(i),"bm{}".format(i))
    edit_files.edit_gender_french("../../data/data-generated/nonames_fr/u{}_fr.csv".format(i),"../../data/data-generated/nonames/u{}.csv".format(i),"u{}".format(i))

#Appending gender with names
for i in range(1,6):
    edit_files.edit_gender_names_french("../../data/data-generated/withnames_fr/bf{}_fr.csv".format(i),"../../data/data-generated/withnames/bf{}.csv".format(i),"bf{}".format(i))
    edit_files.edit_gender_names_french("../../data/data-generated/withnames_fr/bm{}_fr.csv".format(i),"../../data/data-generated/withnames/bm{}.csv".format(i),"bm{}".format(i))
    edit_files.edit_gender_names_french("../../data/data-generated/withnames_fr/u{}_fr.csv".format(i),"../../data/data-generated/withnames/u{}.csv".format(i),"u{}".format(i))
print("Done!")
