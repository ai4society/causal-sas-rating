import pandas as pd



def allure_prep(input_path, dest, count):
    
    data0 = pd.read_csv(input_path)
    
    idx = []
    for u in data0['user']:
        if type(u)==str:
            idx.append(list(data0['user']).index(u))
    
    UB = []
    text = []
    user_gender = []
    temp_no = ct
    c_num = []

    for i in range(len(data0)):
        if i in idx:
            if data0['Gender'][i] == "Prefer not to say":
                temp_gen = 0
                temp_fm = ""
            elif data0['Gender'][i] == "Female":
                temp_gen = 2
                temp_fm = "Hey girl, "
            elif data0['Gender'][i] == "Male":
                temp_gen = 1
                temp_fm = "Hey boy, "         
            temp_no = temp_no + 1
        if data0['conversation.conversation.sender'][i] == "response":
            if data0['conversation.conversation.text'][i] != "text":
                text.append(data0['conversation.conversation.text'][i])
                user_gender.append(temp_gen)
                UB.append(0)
                c_num.append(temp_no)
        elif data0['conversation.conversation.sender'][i] == "client":
            if data0['conversation.conversation.text'][i] != "text":
                user_gender.append(temp_gen)
                UB.append(1)
                text.append(temp_fm + data0['conversation.conversation.text'][i])
                c_num.append(temp_no)
                
                
    df = pd.DataFrame({'C_num': c_num, 'UB': UB, 'User_gender': user_gender, 'Text': text})
    df.to_csv(dest, index=None)
    
    return temp_no



# ALLURE Preprocessing
# The preprocessed files were later combined for experiments.

ct = 0
for i in range(0,3):
    print("Generating ALLURE dataset - {}".format(i))
    ct = allure_prep('../../data/real-world/allure/converted/study{}.csv'.format(i), '../../data/real-world/allure/final/study{}.csv'.format(i), ct)


data_final = pd.read_csv('../../data/real-world/allure/final/final.csv')

texts = []
for each in data_final['Text']:
    texts.append(str(each))
data_final['Text'] = texts

compared = data_final.groupby((data_final['UB'] != data_final['UB'].shift()).cumsum())
combined = compared.agg({'C_num': 'first', 'UB': 'first', 'User_gender': 'first', 'Text': ' '.join}).reset_index(drop=True)

combined.to_csv('../../data/real-world/allure/final/final_expt.csv', index=False)