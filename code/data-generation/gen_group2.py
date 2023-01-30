import pandas as pd
import random
import itertools
import numpy as np













def generate_group(neg_words, pos_words, case_m, case_f, case_n, word_set_no):
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



    sentences = []
    gender_words = male + female
    gender = []
    ems = []
    em_type = ["pos","neg"]



    m_p_c = 0
    m_n_c = 0

    # for p,n in pos_words,neg_words:
    p = pos_words
    n = neg_words
    for t in template:
        for g in male:
            choice = random.choices(em_type,case_m)
            if choice == ["pos"]:
                if len(p) > 1:
                    word = np.random.choice(p)
                else: 
                    word = p[0]
                ems.append(1)
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",g).replace("<person object>",g))
                gender.append(1)
                m_p_c = m_p_c + 1
            elif choice == ["neg"]:
                if len(n) > 1:
                    word = np.random.choice(n)
                else: 
                    word = n[0]
                ems.append(0)
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",g).replace("<person object>",g))
                gender.append(1)
                m_n_c = m_n_c + 1

    f_p_c = 0
    f_n_c = 0
    # for p,n in zip(pos_words,neg_words):    
    # 
 

    for t in template:
        for g in female:
            choice = random.choices(em_type,case_f)
            if choice == ["pos"]:
                if len(p) > 1:
                    word = np.random.choice(p)
                else: 
                    word = p[0]
                ems.append(1)
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",g).replace("<person object>",g))
                gender.append(2)
                f_p_c = f_p_c + 1
            elif choice == ["neg"]:
                if len(n) > 1:
                    word = np.random.choice(n)
                else: 
                    word = n[0]
                ems.append(0)
                sentences.append(t.replace("<emotion word>",word).replace("<person subject>",g).replace("<person object>",g))
                gender.append(2)
                f_n_c = f_n_c + 1

    n_p_c = 0
    n_n_c = 0
    # for p,n in zip(pos_words,neg_words):

  
    for t in template_na:
        choice = random.choices(em_type,case_n)
        if choice == ["pos"]:
            if len(p) > 1:
                word = np.random.choice(p)
            else: 
                word = p[0]
            ems.append(1)
            sentences.append(t.replace("<emotion word>",word))
            gender.append(0)
            n_p_c = n_p_c + 1
        elif choice == ["neg"]:
            if len(n) > 1:
                word = np.random.choice(n)
            else: 
                word = n[0]
            ems.append(0)
            sentences.append(t.replace("<emotion word>",word))
            gender.append(0)
            n_n_c = n_n_c + 1


    final = {'Sentences':sentences,'Gender':gender, 'Emotion':ems}
    print( "There are {} male positive sentences, {} female positive sentences, {} na positive sentences".format(m_p_c,f_p_c,n_p_c))
    (pd.DataFrame.from_dict(final)).to_csv('../../data/data-generated/group2/e{}.csv'.format(word_set_no),index=False)



# Generating datasets
original_data = pd.read_csv("../../data/equity-corpus/Equity-Evaluation-Corpus.csv",engine="python")

emo = list(set(original_data["Emotion word"]))
emo = [each for each in emo if str(each) != 'nan']
emo = sorted(emo)




generate_group([emo[21]], [emo[22]], [0.9,0.1], [0.1,0.9], [0.5,0.5], 3)
generate_group([emo[21],emo[6]], [emo[22]], [0.9,0.1], [0.1,0.9], [0.5,0.5], 4)
generate_group([emo[21]], [emo[18], emo[22]], [0.9,0.1], [0.1,0.9], [0.5,0.5], 5)

print("Group-2 datasets generated.")

# grim, happy, glad, depressing.
# print(emo[21],emo[22],emo[18],emo[6])
