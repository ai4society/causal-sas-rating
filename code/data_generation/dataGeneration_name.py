import pandas as pd
import random



def generate_data():
    original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")
    #original_data.head()

    template = sorted(set(original_data['Template']))
    template = list([template[0],template[4],template[6],template[10]])

    #for i in range(len(template)):
        #print(template[i])

    male = list(sorted(set(original_data[original_data['Gender']=='male']['Person'])))[:10]
    #print(male)
    female = list(sorted(set(original_data[original_data['Gender']=='female']['Person'])))[:10]
    #print(female)

    emo = list(set(original_data["Emotion word"]))
    emo = [each for each in emo if str(each) != 'nan']
    emo = sorted(emo)
    #for each in enumerate(emo):
        #print(each)

    emotion_words = [emo[21],emo[22],emo[4],emo[30],emo[6],emo[16],emo[3],emo[18],emo[28],emo[12]]
    print(emotion_words)
    file_count = 0



    for top in range(0,10,2):
        file_count += 1
        print("This is set {}".format(file_count))

        emotion_word = emotion_words[top:top+2]
        print("Negtive word : '{}' , Positive word : '{}'".format(emotion_word[0],emotion_word[1]))

        sentences = []
        for j in range(len(emotion_word)):
            for k in range(len(template)):
                sentences.append(template[k].replace("<emotion word>",emotion_word[j]))
        sentences = list(sentences)
        gender = ['male','female']
        unbiased_sentences = []
        female_count = 0
        male_count = 0
        gender_name = []

        for m,f in zip(male,female):
            for each in sentences:
                choice = random.choices(gender,[0.5,0.5])
                if(choice == ['male']):
                    unbiased_sentences.append(each.replace("<person object>",m).replace("<person subject>",m))
                    gender_name.append("male")
                    male_count += 1
                elif(choice == ['female']):
                    unbiased_sentences.append(each.replace("<person object>",f).replace("<person subject>",f))
                    gender_name.append("female")
                    female_count += 1

        print("Unbiased set male count is",male_count,"and female count is",female_count)
        (pd.DataFrame.from_dict({'Sentences':unbiased_sentences,'Gender':gender_name})).to_csv('../../data/data-generated/withnames/u{}.csv'.format(file_count),index=False)

        biased_male = []
        female_count = 0
        male_count = 0
        gender_name = []

        for m,f in zip(male,female):
            for each in sentences:
                choice = random.choices(gender,[0.9,0.1])
                if(choice == ['male']):
                    biased_male.append(each.replace("<person object>",m).replace("<person subject>",m))
                    gender_name.append("male")
                    male_count += 1
                elif(choice == ['female']):
                    biased_male.append(each.replace("<person object>",f).replace("<person subject>",f))
                    gender_name.append("female")
                    female_count += 1

        print("biased_male set male count is",male_count,"and female count is",female_count)
        (pd.DataFrame.from_dict({'Sentences':biased_male,'Gender':gender_name})).to_csv('../../data/data-generated/withnames/bm{}.csv'.format(file_count),index=False)

        biased_female = []
        female_count = 0
        male_count = 0
        gender_name = []

        for m,f in zip(male,female):
            for each in sentences:
                choice = random.choices(gender,[0.1,0.9])
                if(choice == ['male']):
                    biased_female.append(each.replace("<person object>",m).replace("<person subject>",m))
                    gender_name.append("male")
                    male_count += 1
                elif(choice == ['female']):
                    biased_female.append(each.replace("<person object>",f).replace("<person subject>",f))
                    gender_name.append("female")
                    female_count += 1

        print("biased_female set male count is",male_count,"and female count is",female_count)
        print()
        (pd.DataFrame.from_dict({'Sentences':biased_female,'Gender':gender_name})).to_csv('../../data/data-generated/withnames/bf{}.csv'.format(file_count),index=False)



generate_data()
