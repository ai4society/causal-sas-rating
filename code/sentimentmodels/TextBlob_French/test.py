from textblob import Blobber
from textblob_fr import PatternTagger, PatternAnalyzer
import pandas as pd

tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
# blob1 = tb(u"Quelle belle matinée")
# print(blob1.sentiment)
# blob2 = tb(u"C'est une voiture terribles.")
# print(blob2.sentiment)

def textblobsentiment_french(path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL, 'fr_FR')
    fr_file = pd.read_csv(path,engine="python",encoding="latin-1")

    sentiment = []
    for each in fr_file['Phrases']:
        sentiment.append((tb(each)).sentiment[0])

    text = []
    for each in fr_file['Phrases']:
        text.append(each)

    gender = []
    for each in fr_file['Gender']:
        gender.append(each)

    d = {'Sentence':text,'Gender':gender,'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])
    final_df.to_csv('../../data/results/textblob/textblob_fr/nonames/{}.csv'.format(file_name),encoding="latin-1")


def textblobsentiment_french_name(path,file_name):
    import locale
    locale.setlocale(locale.LC_ALL,'fr_FR')
    fr_file = pd.read_csv(path,engine="python",encoding="latin-1")

    sentiment = []
    for each in fr_file['Phrases']:
        sentiment.append((tb(each)).sentiment[0])

    text = []
    for each in fr_file['Phrases']:
        text.append(each)

    gender = []
    for each in fr_file['Gender']:
        gender.append(each)

    d = {'Sentence':text,'Gender':gender,'Sentiment':sentiment}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment'])
    final_df.to_csv('../../data/results/textblob/textblob_fr/withnames/{}.csv'.format(file_name),encoding="latin-1")
