import pandas as pd
import random
import itertools
import numpy as np

def generate_group(neg_words, pos_words, case_em, case_ef, case_am, case_af, case_n, word_set_no):
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

    ems = []

    sentences = []
    race_words = euro_male + euro_female + afro_male + afro_female
    gender = []
    race = []

    em_type = ["pos","neg"]
    em_p = 0
    ef_p = 0
    am_p = 0
    af_p = 0
    n_p = 0
    p = pos_words
    n = neg_words

    # for p,n in zip(pos_words,neg_words):
    for t in template:
        for r in euro_male:
            choice = random.choices(em_type,case_em)
            if choice == ["pos"]:
                if len(p) > 1:
                    word = np.random.choice(p)
                else: 
                    word = p[0]
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                ems.append(1)
                gender.append(1)
                race.append(1)
                em_p = em_p + 1
            elif choice == ["neg"]:
                if len(n) > 1:
                    word = np.random.choice(n)
                else: 
                    word = n[0]
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                ems.append(0)
                gender.append(1)
                race.append(1)

# for p,n in zip(pos_words,neg_words):
    for t in template:
        for r in euro_female:
            choice = random.choices(em_type,case_ef)
            if choice == ["pos"]:
                if len(p) > 1:
                    word = np.random.choice(p)
                else: 
                    word = p[0]               
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                ems.append(1)
                gender.append(2)
                race.append(1)
                ef_p = ef_p + 1
            elif choice == ["neg"]:
                if len(n) > 1:
                    word = np.random.choice(n)
                else: 
                    word = n[0]
                ems.append(0)
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                gender.append(2)
                race.append(1)


# for p,n in zip(pos_words,neg_words):
    for t in template:
        for r in afro_male:
            choice = random.choices(em_type,case_am)
            if choice == ["pos"]:
                if len(p) > 1:
                    word = np.random.choice(p)
                else: 
                    word = p[0]
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                ems.append(1)
                gender.append(1)
                race.append(2)
                am_p = am_p + 1
            elif choice == ["neg"]:
                if len(n) > 1:
                    word = np.random.choice(n)
                else: 
                    word = n[0]
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                ems.append(0)
                gender.append(1)
                race.append(2)

# for p,n in zip(pos_words,neg_words):
    for t in template:
        for r in afro_female:
            choice = random.choices(em_type,case_af)
            if choice == ["pos"]:
                if len(p) > 1:
                    word = np.random.choice(p)
                else: 
                    word = p[0]
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                ems.append(1)
                gender.append(2)
                race.append(2)
                af_p = af_p + 1
            elif choice == ["neg"]:
                if len(n) > 1:
                    word = np.random.choice(n)
                else: 
                    word = n[0]
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",r).replace("<person object>",r))
                gender.append(2)
                ems.append(0)
                race.append(2)

# for p,n in zip(pos_words,neg_words):
    for t in template_na:
        choice = random.choices(em_type,case_n)
        if choice == ["pos"]:
            if len(p) > 1:
                word = np.random.choice(p)
            else: 
                word = p[0]
            sentences.append(t.replace("<emotion word>",word))
            ems.append(1)
            gender.append(0)
            race.append(0)
            n_p = n_p + 1
        elif choice == ["neg"]:
            if len(n) > 1:
                word = np.random.choice(n)
            else: 
                word = n[0]
            sentences.append(t.replace("<emotion word>",word))
            ems.append(0)
            gender.append(0)
            race.append(0)
    final = {'Sentences':sentences,'Gender':gender,'Race':race,'Emotion':ems}

    print( "There are {} european male positive sentences, {} european female positive sentences, There are {} african male positive sentences, {} african female positive sentences, {} na positive sentences".format(em_p,ef_p,am_p,af_p,n_p))

    (pd.DataFrame.from_dict(final)).to_csv('../../data/data-generated/group4/e{}.csv'.format(word_set_no),index=False)



# Generating datasets
original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)


generate_group([emo[21]], [emo[22]], [0.9,0.1], [0.5,0.5], [0.5,0.5], [0.1,0.9], [0.5,0.5], 3)
generate_group([emo[21],emo[6]], [emo[22]],  [0.9,0.1], [0.5,0.5], [0.5,0.5], [0.1,0.9], [0.5,0.5], 4)
generate_group([emo[21]], [emo[18], emo[22]],  [0.9,0.1], [0.5,0.5], [0.5,0.5], [0.1,0.9], [0.5,0.5], 5)

print("Group-4 datasets generated.")
