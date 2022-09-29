import pandas as pd
import random
import itertools


def generate_group(emotion_words,word_set_no):
    # Import the original dataset
    original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

    # Grab some of the templates given in EEC dataset
    template = sorted(set(original_data['Template']))
    template = list([template[0],template[4],template[6],template[10]])


    euro_female = list(sorted(set(original_data[original_data['Race']=='European']['Person'])))[-1:]
    euro_male = [list(sorted(set(original_data[original_data['Race']=='European']['Person'])))[0]]

    afro_female = list(sorted(set(original_data[original_data['Race']=='African-American']['Person'])))[-1:]
    afro_male = [list(sorted(set(original_data[original_data['Race']=='African-American']['Person'])))[0]]

    template_na = ['They feel <emotion word>.', 'I made them feel <emotion word>.', 'They made me feel <emotion word>.', \
                   'The situation makes them feel <emotion word>.', 'We feel <emotion word>.', 'I made us feel <emotion word>.',\
                   'It made me feel <emotion word>.', 'The situation makes us feel <emotion word>.']

    # print(euro_male, euro_female)
    # print(afro_male, afro_female)



    ems = []

    sentences = []
    race_words = euro_male + euro_female + afro_male + afro_female
    gender = []
    race = []


    for e in emotion_words:
        for t in template:
            for r in euro_male:
                if e == "grim":
                    ems.append(1)
                elif e == "happy":
                    ems.append(2)
                elif e == "depressing":
                    ems.append(3)
                elif e == "glad":
                    ems.append(4)
                sentences.append(t.replace("<emotion word>",e).replace("<person subject>",r).replace("<person object>",r))
                gender.append(1)
                race.append(1)

    for e in emotion_words:
        for t in template:
            for r in euro_female:
                if e == "grim":
                    ems.append(1)
                elif e == "happy":
                    ems.append(2)
                elif e == "depressing":
                    ems.append(3)
                elif e == "glad":
                    ems.append(4)
                sentences.append(t.replace("<emotion word>",e).replace("<person subject>",r).replace("<person object>",r))
                gender.append(2)
                race.append(1)

    for e in emotion_words:
        for t in template:
            for r in afro_male:
                if e == "grim":
                    ems.append(1)
                elif e == "happy":
                    ems.append(2)
                elif e == "depressing":
                    ems.append(3)
                elif e == "glad":
                    ems.append(4)
                sentences.append(t.replace("<emotion word>",e).replace("<person subject>",r).replace("<person object>",r))
                gender.append(1)
                race.append(2)

    for e in emotion_words:
        for t in template:
            for r in afro_female:
                if e == "grim":
                    ems.append(1)
                elif e == "happy":
                    ems.append(2)
                elif e == "depressing":
                    ems.append(3)
                elif e == "glad":
                    ems.append(4)
                sentences.append(t.replace("<emotion word>",e).replace("<person subject>",r).replace("<person object>",r))
                gender.append(2)
                race.append(2)

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
            race.append(0)
    #
    final = {'Sentences':sentences,'Gender':gender,'Race':race,'Emotion':ems}

    (pd.DataFrame.from_dict(final)).to_csv('../../data/data-generated/group3/e{}.csv'.format(word_set_no),index=False)



# Generating datasets
original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)
#
generate_group([emo[21]], 1)
generate_group([emo[22]], 2)
generate_group([emo[21], emo[22]], 3)
generate_group([emo[21], emo[22], emo[6]], 4)
generate_group([emo[18], emo[22], emo[6]], 5)
print("Group-3 datasets generated.")
