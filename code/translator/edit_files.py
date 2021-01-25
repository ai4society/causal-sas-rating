import pandas as pd

# making data frame from csv file
#data = pd.read_csv("bm2_french.csv",engine="python")

# dropping passed columns
#data.drop([" sexe"], axis = 1, inplace = True)

def edit_gender(path,en_path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL,'fr_FR')
    data = pd.read_csv(path,engine="python",encoding="latin-1")

    data.drop([" sexe"], axis = 1, inplace = True)

    data_en = pd.read_csv(en_path,engine="python")

    data['Gender'] = data_en['Gender']



    data.to_csv("../../data/data-generated/withnames_french/{}_fr.csv".format(file_name),encoding="latin-1")


def edit_gender_names(path,en_path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL,'fr_FR')
    data = pd.read_csv(path,engine="python",encoding="latin-1")

    data.drop([" sexe"], axis = 1, inplace = True)

    data_en = pd.read_csv(en_path,engine="python")

    data['Gender'] = data_en['Gender']

    data.to_csv("../../data/data-generated/nonames_french/{}_fr.csv".format(file_name),encoding="latin-1")



edit_gender("../../data/data-generated/withnames_french/bf1_fr.csv","../../data/data-generated/withnames/bf1.csv","bf1")
edit_gender("../../data/data-generated/withnames_french/bf2_fr.csv","../../data/data-generated/withnames/bf2.csv","bf2")
edit_gender("../../data/data-generated/withnames_french/bf3_fr.csv","../../data/data-generated/withnames/bf3.csv","bf3")
edit_gender("../../data/data-generated/withnames_french/bf4_fr.csv","../../data/data-generated/withnames/bf4.csv","bf4")
edit_gender("../../data/data-generated/withnames_french/bf5_fr.csv","../../data/data-generated/withnames/bf5.csv","bf5")
edit_gender("../../data/data-generated/withnames_french/bm1_fr.csv","../../data/data-generated/withnames/bm1.csv","bm1")
edit_gender("../../data/data-generated/withnames_french/bm2_fr.csv","../../data/data-generated/withnames/bm2.csv","bm2")
edit_gender("../../data/data-generated/withnames_french/bm3_fr.csv","../../data/data-generated/withnames/bm3.csv","bm3")
edit_gender("../../data/data-generated/withnames_french/bm4_fr.csv","../../data/data-generated/withnames/bm4.csv","bm4")
edit_gender("../../data/data-generated/withnames_french/bm5_fr.csv","../../data/data-generated/withnames/bm5.csv","bm5")
edit_gender("../../data/data-generated/withnames_french/u1_fr.csv","../../data/data-generated/withnames/u1.csv","u1")
edit_gender("../../data/data-generated/withnames_french/u2_fr.csv","../../data/data-generated/withnames/u2.csv","u2")
edit_gender("../../data/data-generated/withnames_french/u3_fr.csv","../../data/data-generated/withnames/u3.csv","u3")
edit_gender("../../data/data-generated/withnames_french/u4_fr.csv","../../data/data-generated/withnames/u4.csv","u4")
edit_gender("../../data/data-generated/withnames_french/u5_fr.csv","../../data/data-generated/withnames/u5.csv","u5")



edit_gender_names("../../data/data-generated/nonames_french/bf1_fr.csv","../../data/data-generated/nonames/bf1.csv","bf1")
edit_gender_names("../../data/data-generated/nonames_french/bf2_fr.csv","../../data/data-generated/nonames/bf2.csv","bf2")
edit_gender_names("../../data/data-generated/nonames_french/bf3_fr.csv","../../data/data-generated/nonames/bf3.csv","bf3")
edit_gender_names("../../data/data-generated/nonames_french/bf4_fr.csv","../../data/data-generated/nonames/bf4.csv","bf4")
edit_gender_names("../../data/data-generated/nonames_french/bf5_fr.csv","../../data/data-generated/nonames/bf5.csv","bf5")
edit_gender_names("../../data/data-generated/nonames_french/bm1_fr.csv","../../data/data-generated/nonames/bm1.csv","bm1")
edit_gender_names("../../data/data-generated/nonames_french/bm2_fr.csv","../../data/data-generated/nonames/bm2.csv","bm2")
edit_gender_names("../../data/data-generated/nonames_french/bm3_fr.csv","../../data/data-generated/nonames/bm3.csv","bm3")
edit_gender_names("../../data/data-generated/nonames_french/bm4_fr.csv","../../data/data-generated/nonames/bm4.csv","bm4")
edit_gender_names("../../data/data-generated/nonames_french/bm5_fr.csv","../../data/data-generated/nonames/bm5.csv","bm5")
edit_gender_names("../../data/data-generated/nonames_french/u1_fr.csv","../../data/data-generated/nonames/u1.csv","u1")
edit_gender_names("../../data/data-generated/nonames_french/u2_fr.csv","../../data/data-generated/nonames/u2.csv","u2")
edit_gender_names("../../data/data-generated/nonames_french/u3_fr.csv","../../data/data-generated/nonames/u3.csv","u3")
edit_gender_names("../../data/data-generated/nonames_french/u4_fr.csv","../../data/data-generated/nonames/u4.csv","u4")
edit_gender_names("../../data/data-generated/nonames_french/u5_fr.csv","../../data/data-generated/nonames/u5.csv","u5")
