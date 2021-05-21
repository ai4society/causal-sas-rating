# Rating of Sentiment Models for Bias


Steps to run the experiments:

1) Go to code/data_generation/ from your command terminal and run the .py files (dataGeneration.py, dataGeneration_name.py,dataGeneration_baseline.py)
   which will generate the data required for the experiments.

2) Go to code/translator/ from your command terminal and run 'tran_fr.py' file to translate the same data into French.

3) In the same directory, run 'tran_fr_oto.py' file to translate the French datasets back to OTO (English). Now we have all the data needed for 
   the experiments.

4) Go to code/sentimentmodels/, follow the instructions in the readme file inside that directory to evaluate all the SAS on generated datasets including
   the baseline calculation.

5) Go to code/translator/ and run 'calc.py' file to see different stats like gender and word difference when the sentences are translated from English
   to French and back to English. These stats will be generated in 'data/results/analaysis' directory.
