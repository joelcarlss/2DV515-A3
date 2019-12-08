import pandas as pd
import pickle
from document_data import *


# Requires that page rank already exists. It is saved for it self
def merge_save_data_frames():
	df, dictionary = get_document_data()
	page_rank = pd.read_pickle('pagerank.pkl')
	merged_df = pd.merge(df, page_rank, on='name')
	merged_df.to_pickle('dataframe.pkl')

	with open('dictionary.pkl', 'wb') as handle:
		pickle.dump(merged_df, handle, protocol=pickle.HIGHEST_PROTOCOL)


def load_data_from_file():
	df = pd.read_pickle('dataframe.pkl')
	with open('filename.pickle', 'rb') as handle:
		dictionary = pickle.load(handle)



def words_to_index(words):
	indexes = []
	for word in words:
		if word in dictionary:
			indexes.append(dictionary[word])
	return indexes


# Return all documents including word
def get_all_occurrences(index_list):
	result = []
	for a in df:
		if any(item in index_list for item in a[0]): # Exchange for np.in1d(a[0], index_list)
			result.append(a)

	return result

