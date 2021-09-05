import google_trans_new
from google_trans_new import google_translator
import pandas as pd

translator = google_translator()

def tran_french(path,file_name):

    upload_file = open(path, "r")
    text= upload_file.read()
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt="fr")
    upload_file.close()

    translated_file = open ("../../data/data-generated/nonames_fr/{}_fr.csv".format(file_name),"w")
    translated_file.write (translated_text)
    translated_file.close()

def tran_french_names(path,file_name):

    upload_file = open(path, "r")
    text= upload_file.read()
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt="fr")
    upload_file.close()

    translated_file = open ("../../data/data-generated/withnames_fr/{}_fr.csv".format(file_name),"w")
    translated_file.write (translated_text)
    translated_file.close()


def tran_oto(path,file_name):

    upload_file = open(path, "r")
    text= upload_file.read()
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt="en")
    upload_file.close()

    translated_file = open("../../data/data-generated/nonames_fr_oto/{}_fr_oto.csv".format(file_name),"w",encoding="utf-8")
    translated_file.write(translated_text)
    translated_file.close()

def tran_oto_names(path,file_name):

    upload_file = open(path, "r")
    text= upload_file.read()
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt="en")
    upload_file.close()

    translated_file = open("../../data/data-generated/withnames_fr_oto/{}_fr_oto.csv".format(file_name),"w",encoding="utf-8")
    translated_file.write(translated_text)
    translated_file.close()

#German translation
#There is an issue with google translator. If you face any error like 'json.decoder.JSONDecodeError..', edit line 151 of 'google_trans_new.py'
#in your site packages to 'response = decoded_line'
def tran_german(path,file_name):
    data = pd.read_csv(path)
    countRows = (len(data))

    translatedCSV = { "Sentences":[], "Gender":[]}

    #Translated word one by one from the CSV file and save them to the dictionary
    for index, row in data.iterrows():
        translatedCSV["Sentences"].append(translator.translate(row["Sentences"], lang_tgt="de"))
        translatedCSV["Gender"].append(translator.translate(row["Gender"], lang_tgt="de"))

    #Create a Dataframe from Dictionary
    #Save the DataFrame to a CSV file
    df = pd.DataFrame(data=translatedCSV)
    df.to_csv("../../data/data-generated/nonames_de/{}_de.csv".format(file_name))

    #
    # upload_file = open(path, "r")
    # text= upload_file.read()
    # translator = google_translator()
    # translated_text = translator.translate(text, lang_tgt="de")
    # upload_file.close()
    #
    # translated_file = open ("../../data/data-generated/nonames_de/{}_de.csv".format(file_name),"w")
    # translated_file.write (translated_text)
    # translated_file.close()

def tran_german_names(path,file_name):

    data = pd.read_csv(path)
    countRows = (len(data))

    translatedCSV = { "Sentences":[], "Gender":[]}

    #Translated word one by one from the CSV file and save them to the dictionary
    for index, row in data.iterrows():
        translatedCSV["Sentences"].append(translator.translate(row["Sentences"], lang_tgt="de"))
        translatedCSV["Gender"].append(translator.translate(row["Gender"], lang_tgt="de"))

    #Create a Dataframe from Dictionary
    #Save the DataFrame to a CSV file
    df = pd.DataFrame(data=translatedCSV)
    df.to_csv("../../data/data-generated/withnames_de/{}_de.csv".format(file_name))

    # upload_file = open(path, "r")
    # text= upload_file.read()
    # translator = google_translator()
    # translated_text = translator.translate(text, lang_tgt="de")
    # upload_file.close()
    #
    # translated_file = open ("../../data/data-generated/withnames_de/{}_de.csv".format(file_name),"w")
    # translated_file.write (translated_text)
    # translated_file.close()

# def importCSV():
#     data = pd.read_csv('bf1.csv')
#     countRows = (len(data))
#
#     translatedCSV = { "Sentences":[]}
#
#     #Translated word one by one from the CSV file and save them to the dictionary
#     for index, row in data.iterrows():
#         translatedCSV["Sentences"].append(translator.translate(row["Sentences"], lang_tgt="de"))
#
#     #Create a Dataframe from Dictionary
#     #Save the DataFrame to a CSV file
#     df = pd.DataFrame(data=translatedCSV)
#     df.to_csv("translatedCSV.csv", sep='\t')
#
# importCSV()
