Run the following command to generate results for datasets with relations like mom and dad as gender variables using either vader, textblob, cnn, lstm or gru.

             python evaluate.py --model <model_name>

Ex:  python evaluate.py --model textblob
     python evaluate.py --model vader
     python evaluate.py --model cnn
     python evaluate.py --model lstm
     python evaluate.py --model gru



Run the following command to generate results for datasets with person names as gender variables using either vader, textblob or cnn, lstm or gru.

	     python evaluate_name.py --model <model_name>

Ex:  python evaluate_name.py --model textblob
     python evaluate_name.py --model vader
     python evaluate_name.py --model cnn
     python evaluate_name.py --model gru
     python evaluate_name.py --model lstm