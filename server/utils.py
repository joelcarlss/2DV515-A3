import pandas as pd
import numpy as np
from db import *
import glob

def get_read_data():
	df = pd.read_pickle(file_name)

def get_data():
	list_of_files = glob.glob('./wikipedia/Words/*/*')  # create the list of file
	df = pd.DataFrame(columns=['text', 'name', 'category'])
	dict = {}

	for file_name in list_of_files:
		path = str.split(file_name, '/')
		file = open(file_name).read()
		file = file.replace('.', '')
		array = file.split(' ')[:-1]
		int_array = []
		for word in array:
			if word not in dict:
				dict[word] = len(dict)
			int_array.append(dict[word])

		int_array = np.array(int_array)
		df = df.append({'text': int_array, 'name': path[4], 'category': path[3]}, ignore_index=True)
		df = pd.DataFrame(df) # TODO: remove
	df = df.to_numpy()
	return df, dict

df, dictionary = get_data()


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

