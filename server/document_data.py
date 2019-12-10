import glob
import pandas as pd
import numpy as np


def get_document_data():
	list_of_files = glob.glob('./wikipedia/Words/*/*')  # create the list of file
	df = pd.DataFrame(columns=['text', 'name', 'category', 'filename'])
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
		df = df.append({'text': int_array, 'name': path[4], 'category': path[3], 'filename': file_name}, ignore_index=True)
		df = pd.DataFrame(df) # TODO: remove
	return df, dict

