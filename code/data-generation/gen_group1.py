import pandas as pd
import random
import itertools


def generate_group(emotion_words,word_set_no):
    # Import the original dataset
    original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

    # Grab some of the templates given in EEC dataset
    template = sorted(set(original_data['Template']))
    template = list([template[0],template[4],template[6],template[10]])


    male = list(sorted(set(original_data[original_data['Gender']=='male']['Person'])))[-2:]
    male[0] = male[0].replace("him","my nephew")

    female = list(sorted(set(original_data[original_data['Gender']=='female']['Person'])))[-2:]

    template_na = ['They feel <emotion word>.', 'I made them feel <emotion word>.', 'They made me feel <emotion word>.', \
                   'The situation makes them feel <emotion word>.', 'We feel <emotion word>.', 'I made us feel <emotion word>.',\
                   'It made me feel <emotion word>.', 'The situation makes us feel <emotion word>.']

    # print("the male and female gender variables are: \n")
    # print(male)
    # print(female)



    # emo = list(set(original_data["Emotion word"]))
    # emo = [each for each in emo if str(each) != 'nan']
    # emo = sorted(emo)

    # emotion_words = [emo[21]]

    # ems = list(itertools.repeat(1, len(emotion_words)*8*3))

    sentences = []
    gender_words = male + female
    gender = []
    ems = []

    # print(templates[-8:])



    for e in emotion_words:
        for t in template:
            for g in male:
                if e == "grim":
                    ems.append(1)
                elif e == "happy":
                    ems.append(2)
                elif e == "depressing":
                    ems.append(3)
                elif e == "glad":
                    ems.append(4)
                sentences.append(t.replace("<emotion word>",e).replace("<person subject>",g).replace("<person object>",g))
                gender.append(1)


    for e in emotion_words:
        for t in template:
            for g in female:
                if e == "grim":
                    ems.append(1)
                elif e == "happy":
                    ems.append(2)
                elif e == "depressing":
                    ems.append(3)
                elif e == "glad":
                    ems.append(4)
                sentences.append(t.replace("<emotion word>",e).replace("<person subject>",g).replace("<person object>",g))
                gender.append(2)



    for e in emotion_words:
        for t in template_na:
            if e == "grim":
                ems.append(1)
            elif e == "happy":
                ems.append(2)
            elif e == "depressing":
                ems.append(3)
            elif e == "glad":
                ems.append(4)
            sentences.append(t.replace("<emotion word>",e))
            gender.append(0)

    final = {'Sentences':sentences,'Gender':gender, 'Emotion':ems}

    (pd.DataFrame.from_dict(final)).to_csv('../../data/data-generated/group1/e{}.csv'.format(word_set_no),index=False)



# Generating datasets
original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)

generate_group([emo[21]], 1)
generate_group([emo[22]], 2)
generate_group([emo[21], emo[22]], 3)
generate_group([emo[21], emo[22], emo[6]], 4)
generate_group([emo[18], emo[22], emo[6]], 5)
print("Group-1 datasets generated.")


# [emo[22], emo[6], emo[]]
