from textblob import Blobber
from textblob_de import TextBlobDE as TextBlob
import pandas as pd


def textblobsentiment_german(path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL, 'de_DE')
    ge_file = pd.read_csv(path,engine="python",encoding="latin-1")

    sentiment = []
    for each in ge_file['Sentences']:
        sentiment.append((TextBlob(each)).sentiment[0])

    text = []
    for each in ge_file['Sentences']:
        text.append(each)

    gender = []
    for each in ge_file['Gender']:
        gender.append(each)

    d = {'Sentence':text,'Gender':gender,'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])
    final_df.to_csv('../../data/results/textblob/textblob_de/nonames/{}.csv'.format(file_name),encoding="latin-1",index=False)


def textblobsentiment_german_name(path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL,'de_DE')
    de_file = pd.read_csv(path,engine="python",encoding="latin-1")

    sentiment = []
    for each in de_file['Sentences']:
        sentiment.append((TextBlob(each)).sentiment[0])

    text = []
    for each in de_file['Sentences']:
        text.append(each)

    gender = []
    for each in de_file['Gender']:
        gender.append(each)

    d = {'Sentence':text,'Gender':gender,'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])
    final_df.to_csv('../../data/results/textblob/textblob_de/withnames/{}.csv'.format(file_name),encoding="latin-1",index=False)
