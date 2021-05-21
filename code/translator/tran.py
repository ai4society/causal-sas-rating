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
