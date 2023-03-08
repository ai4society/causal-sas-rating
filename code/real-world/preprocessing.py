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


# Access the combined dataset and merge all the consecutive utterances from the same user or chatbot into one single utterance for the ease of experimenting.

data_final = pd.read_csv('../../data/real-world/allure/final/final.csv')

texts = []
for each in data_final['Text']:
    texts.append(str(each))
data_final['Text'] = texts

compared = data_final.groupby((data_final['UB'] != data_final['UB'].shift()).cumsum())
combined = compared.agg({'C_num': 'first', 'UB': 'first', 'User_gender': 'first', 'Text': ' '.join}).reset_index(drop=True)

combined.to_csv('../../data/real-world/allure/final/final_expt.csv', index=False)
print("The final preprocessed dataset can be found here: \n")
print('../../data/real-world/allure/final/final_expt.csv')



## University chatbot preprocessing
data = pd.read_csv('../../data/real-world/unibot/converted/conv.csv')

cols = data.columns

# Merge all the columns.
data['combo'] = data.apply(lambda x: ', '.join([str(each) for each in x]), axis=1)

# Drop the original columns
data = data.drop(labels=list(cols), axis=1)

# The data is seperated by the delimiter, '|'. Now, separate the attributes.

text = []
for each in data['combo']:
    temp_text = str(each).replace(', nan','')
    temp_text = temp_text.split('|')
    text.append(temp_text)

# Filter the dataset completely.

UB = []
response = []
ct = 1
count = []
for each in text:
    if len(each) == 9:
        if '/greet' in str(each[8]):
            response.append("Hi")
            count.append(ct)
        elif 'helpfulness' in str(each[8]):
            response.append("helpful")
            count.append(ct)       
        elif 'Ôºü' in str(each[8]):
            response.append(each[8].replace("Ôºü","?"))  
            count.append(ct)          
        elif '‚Äôs' in str(each[8]):
            response.append(each[8].replace("‚Äôs","'s"))
            count.append(ct)
        elif 'versation ended' in str(each[8]):
            count.append(ct)
            ct = ct + 1
            response.append(each[8].replace("„ÄêConversation ended„Äë",""))
        else:
            count.append(ct)
            response.append(each[8])
        UB.append(each[2])
    elif len(each) == 6:
        if '/greet' in str(each[4]):
            response.append("Hi")
            count.append(ct)
        elif 'helpfulness' in str(each[4]):
            response.append("helpful")
            count.append(ct)    
        elif 'Ôºü' in str(each[4]):
            response.append(each[4].replace("Ôºü","?")) 
            count.append(ct)  
        elif '‚Äôs' in str(each[4]):
            response.append(each[4].replace("‚Äôs","'s"))
            count.append(ct)
        elif 'versation ended' in str(each[4]):
            count.append(ct)
            ct = ct + 1
            response.append(each[4].replace("„ÄêConversation ended„Äë",""))
        else:
            if '_' in each[4]:
                count.append(ct)
                response.append(each[4].replace('_',' ').split(" ")[0])
            else:
                count.append(ct)
                response.append(each[4])
        UB.append(each[2])
    elif len(each) == 1:
        if 'versation ends' in str(each[0]):
            ct = ct + 1
        elif 'versation ended' in str(each[0]):
            ct = ct + 1
        else:
            count.append(ct)
            UB.append('B')
            response.append(each[0])

for u,r,c in zip(UB,response,count):
    if r == " ":
        UB.remove(u)
        response.remove(r)
        count.remove(c)

UB1 = []
for u in UB:
    if "B" in str(u): UB1.append(0)
    else: UB1.append(1)
    
    

response1 = []
ori = []
addn = []
gender = []

for u,r,c in zip(UB1,response,count):
    if c in range(1,12):
        if u == 1:
            response1.append("Hey, " + str(r))
            ori.append(str(r))
            addn.append("Hey, ")
            gender.append(0)
        else:
            response1.append(str(r))
            ori.append(str(r))
            addn.append("No enhancement")
            gender.append(0)
    elif c in range(12,22):
        if u == 1:
            response1.append("Hey boy, " + str(r))
            ori.append(str(r))
            addn.append("Hey boy, ")
            gender.append(1)
        else:
            response1.append(str(r))
            ori.append(str(r))
            gender.append(1)
            addn.append("No enhancement")
    elif c in range(22,32):
        if u == 1:
            response1.append("Hey girl, " + str(r))
            ori.append(str(r))
            addn.append("Hey girl, ")
            gender.append(2)
        else:
            response1.append(str(r))
            ori.append(str(r))
            addn.append("No enhancement")
            gender.append(2)
 
 
 
df = pd.DataFrame({'C_num': count, 'UB': UB1, 'User_gender': gender, 'Original': ori, 'Enhancement': addn, 'Text': response1})
df.to_csv('../../data/real-world/unibot/final/final.csv', index=None) 

# Access the combined dataset and merge all the consecutive utterances from the same user or chatbot into one single utterance for the ease of experimenting.

data_final = pd.read_csv('../../data/real-world/unibot/final/final.csv')

texts = []
for each in data_final['Text']:
    texts.append(str(each))
data_final['Text'] = texts

compared = data_final.groupby((data_final['UB'] != data_final['UB'].shift()).cumsum())
combined = compared.agg({'C_num': 'first', 'UB': 'first', 'User_gender': 'first', 'Original': 'first', 'Enhancement': 'first', 'Text': ' '.join}).reset_index(drop=True)

combined.to_csv('../../data/real-world/unibot/final/final_expt.csv', index=False)
print("The final preprocessed dataset can be found here: \n")
print('../../data/real-world/allure/unibot/final_expt.csv')