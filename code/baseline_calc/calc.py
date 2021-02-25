import pandas as pd

original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)

emotion_words = [emo[21],emo[22],emo[4],emo[30],emo[6],emo[16],emo[3],emo[18],emo[28],emo[12]]

#Calculating averages for each sentences with each of the emotion words.
def run_calc():
    for word in emotion_words:
        data = pd.read_csv("../../data/baseline/{}_sentiment.csv".format(word))
        average = (data.sum(axis=1))/6

        data['Average_Sentiment'] = average
        data.to_csv("../../data/baseline/{}_sentiment.csv".format(word),index=False)

#run_calc()

#Total of the averages for sentences having each of the emotion words.
def total_average():
    average = []
    for word in emotion_words:
        data = pd.read_csv("../../data/baseline/{}_sentiment.csv".format(word))
        average.append((data['Average_Sentiment'].sum())/80)
    d = {'Word':emotion_words,'Average Sentiment':average}
    df = pd.DataFrame(d, columns=['Word','Average Sentiment'])
    df.to_csv("../../data/baseline/averages.csv",index=False)

        #print("average for {} is {}".format(word,average))
total_average()
