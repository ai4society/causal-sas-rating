import pandas as pd

def edit_gender(path,en_path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL,'fr_FR')
    data = pd.read_csv(path,engine="python",encoding="latin-1")

    data.drop([" genre"], axis = 1, inplace = True)

    data_en = pd.read_csv(en_path,engine="python")

    data['Gender'] = data_en['Gender']



    data.to_csv("../../data/data-generated/nonames_fr/{}_fr.csv".format(file_name),encoding="latin-1")


def edit_gender_names(path,en_path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL,'fr_FR')
    data = pd.read_csv(path,engine="python",encoding="latin-1")

    data.drop([" genre"], axis = 1, inplace = True)

    data_en = pd.read_csv(en_path,engine="python")

    data['Gender'] = data_en['Gender']

    data.to_csv("../../data/data-generated/withnames_fr/{}_fr.csv".format(file_name),encoding="latin-1")
