# causal-sas-rating

# Steps to run the original rating algorithm

Step-0 (prerequisites): Run 'conda create --name <env> --file requirements.txt' to install all the required prerequisites on your windows system.

Step-1 (Data Generation): Each of the files (gen_groupX.py) in 'code/data-generation' directory generates different data groups for the experiments. The 'composite.py' file in the same location generates data for the experiments in which we used composite data (race + gender).


Step-2 (Sentiment Analysis): In 'code/', run 'eval_groupX.py' files to get the results from each of the SASs for different data groups.


Step-3 (Rating of SASs): In 'code/rating/', run the rating.py file to get the fine-grained and overall ratings for each of the SASs.
  
# Steps to run the rating algorithm on real-world datasets and evaluate them.
  
Step-0 (prerequisites): Run 'conda create --name <env> --file requirements.txt' to install all the required prerequisites on your windows system.

Step-1 (Pre-processed real-world datasets): We have 2 datasets: ALLURE chatbot conversations dataset and Unibot conversations dataset. 
(a) ALLURE dataset is in 'data/real-world/allure/final'. The file 'final.csv' has multiple consecutive utterances of the chatbot in multiple lines but 'final_expt.csv' file has multiple consecutive utterances of the chatbot in the same line (this is much better for experiments). 
(b) Unibot dataset is in 'data/real-world/unibot/final'. The file 'final.csv' has multiple consecutive utterances of the chatbot in multiple lines but 'final_expt.csv' file has multiple consecutive utterances of the chatbot in the same line (again, this is much better for experiments). 


Step-2 (Sentiment Analysis): In 'code/', run 'eval_data.py' files to get the results from each of the SASs for different both datasets: ALLURE and Unibot.


Step-3 (Rating of SASs): In 'code/rating/', run the rating.py file to get the fine-grained and overall ratings for each of the SASs based on the real-world data.
  
