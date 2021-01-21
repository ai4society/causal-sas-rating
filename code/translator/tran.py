import google_trans_new
from google_trans_new import google_translator
import pandas as pd

translator = google_translator()


#Source: https://duyguaran.medium.com/how-to-use-google-trans-new-346ab827a4eb

def tran_french(path,file_name):
    #upload_file = open(path,"r")
    #text= upload_file.read()
    upload_file = open(path, "r")
    text= upload_file.read()
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt="fr")
    upload_file.close()

    translated_file = open ("../../data/data-generated/nonames_french/{}_fr.csv".format(file_name),"w")
    translated_file.write (translated_text)
    translated_file.close()

def tran_french_names(path,file_name):
    #upload_file = open(path,"r")
    #text= upload_file.read()
    upload_file = open(path, "r")
    text= upload_file.read()
    translator = google_translator()
    translated_text = translator.translate(text, lang_tgt="fr")
    upload_file.close()

    translated_file = open ("../../data/data-generated/withnames_french/{}_fr.csv".format(file_name),"w")
    translated_file.write (translated_text)
    translated_file.close()

def append_gender(path,file_name):

    set_en = pd.read_csv(path,engine="python")
    set_fr = pd.read_csv("../../data/data-generated/nonames_french/{}_fr.csv".format(file_name),engine="python")
    d = {'Sentences':set_fr['Sentences'], 'Gender':set_en['Gender']}
    final_df = pd.DataFrame(d, columns=['Sentences','Gender'])
    final_df.to_csv("../../data/data-generated/nonames_french/{}_fr.csv".format(file_name))
