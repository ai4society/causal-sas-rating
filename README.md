# causal-sas-rating
Step-0 (prerequisites): Run 'conda create --name <env> --file requirements.txt' to install all the required prerequisites on your windows system.

Step-1 (Data Generation): Each of the files (gen_groupX.py) in 'code/data-generation' directory generates different data groups for the experiments. The 'composite.py' file in the same location generates data for the experiments in which we used composite data (race + gender).


Step-2 (Sentiment Analysis): In 'code/', run 'eval_groupX.py' files to get the results from each of the SASs for different data groups.


Step-3 (Rating of SASs): In 'code/rating/', run the rating.py file to get the fine-grained and overall ratings for each of the SASs.
