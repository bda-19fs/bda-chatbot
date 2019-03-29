import pandas as pd
import pickle

if __name__ == '__main__':
	csv = pd.read_csv('bda_id_whitelist.csv', sep='\t', usecols=[0])
	list = csv.values.flatten().tolist()
	pickle.dump(list, open('bda_article_ids.pickle', 'wb'))