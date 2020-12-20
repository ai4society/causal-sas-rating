from textblob import TextBlob
import nltk
import pandas as pd


"""
Input: path for dataset which is to be analyzed,
       name with which the result should be stored.
Output: Result datasets will be generated.
"""
def textblobsentiment(path,file_name):
    set = pd.read_csv(path,engine="python")

    senti = []
    for each in set['Sentences']:
        senti.append(TextBlob(each))

    sentiment = []
    for each in senti:
        sentiment.append(each.sentiment[0])
    subjectivity = []
    for each in senti:
        subjectivity.append(each.sentiment[1])
    text = []
    for each in set['Sentences']:
        text.append(each)

    d = {'Sentence':text,'Gender':set['Gender'],'Sentiment':sentiment,'Subjectivity':subjectivity}
    final_df = pd.DataFrame(d, columns=['Sentence','Gender','Sentiment','Subjectivity'])

    final_df.to_csv('../../data/results/textblob/{}.csv'.format(file_name))
