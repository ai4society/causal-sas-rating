In the 'Translator' directory, we have used TextBlob results (Sentiment scores for English, French and OTO) to translate the datasets to French and back to English (OTO) again.
We also calculated the gender and word difference when these are translated back to English (OTO). 
Follow the below steps carefully to replicate our results.

Translation:
1. Go to the 'Translator' directory and run 'tran_fr.py' file to translate the original English dataset to French.
2. Go to the 'Translator' directory and run 'tran_fr_oto.py' file to translate the French dataset from the above step back to English (OTO).

Translation Calculation (Need some better heading):
1. Follow step-7 directly to replicate the results. Steps 2-6 have description of each file in this directory.
2. While translating French datasets to English, some of the column names were not formatted properly. To handle such issues, we have created 'edit_files.py'.
3. When translated back to OTO, we checked if the gender variables have been translated correctly. You might not see any gender difference for the dataset with names.
   The code for this was written in 'gender_diff.py' file
4. In 'tran_senti_avg.py', we have written the code for calculating the average sentiment scores for all the sentences together for all the TextBlob results datasets.
5. We calculated the sentiment score difference between original english dataset and French to OTO dataset for with and without names in 'trans_senti_diff.py' file.
6. For each of the pairs, we have calculated the difference between the words in the same sentences in English and OTO datasets. This code can be found in 'word_diff.py' dataset.
7. Just run 'calc.py' file in this directory to perform all these calculations in one go.

