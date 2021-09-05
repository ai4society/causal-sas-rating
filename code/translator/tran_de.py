import tran
from tran import tran_german,tran_german_names
import edit_files


#Without names
# for i in range(1,6):
#     print("Generating German dataset {}/5 without names".format(i))
#     tran_german("../../data/data-generated/nonames/bf{}.csv".format(i),"bf{}".format(i))
#     tran_german("../../data/data-generated/nonames/bm{}.csv".format(i),"bm{}".format(i))
#     tran_german("../../data/data-generated/nonames/u{}.csv".format(i),"u{}".format(i))

#With names.
# for i in range(1,6):
#     print("Generating German dataset {}/5 with names".format(i))
#     tran_german_names("../../data/data-generated/withnames/bf{}.csv".format(i),"bf{}".format(i))
#     tran_german_names("../../data/data-generated/withnames/bm{}.csv".format(i),"bm{}".format(i))
#     tran_german_names("../../data/data-generated/withnames/u{}.csv".format(i),"u{}".format(i))

#Appending gender without names
print("Changing gender names from German to English")
for i in range(1,6):
    edit_files.edit_gender_german("../../data/data-generated/nonames_de/bf{}_de.csv".format(i),"../../data/data-generated/nonames/bf{}.csv".format(i),"bf{}".format(i))
    edit_files.edit_gender_german("../../data/data-generated/nonames_de/bm{}_de.csv".format(i),"../../data/data-generated/nonames/bm{}.csv".format(i),"bm{}".format(i))
    edit_files.edit_gender_german("../../data/data-generated/nonames_de/u{}_de.csv".format(i),"../../data/data-generated/nonames/u{}.csv".format(i),"u{}".format(i))

#Appending gender with names
for i in range(1,6):
    edit_files.edit_gender_names_german("../../data/data-generated/withnames_de/bf{}_de.csv".format(i),"../../data/data-generated/withnames/bf{}.csv".format(i),"bf{}".format(i))
    edit_files.edit_gender_names_german("../../data/data-generated/withnames_de/bm{}_de.csv".format(i),"../../data/data-generated/withnames/bm{}.csv".format(i),"bm{}".format(i))
    edit_files.edit_gender_names_german("../../data/data-generated/withnames_de/u{}_de.csv".format(i),"../../data/data-generated/withnames/u{}.csv".format(i),"u{}".format(i))
print("Done!")
