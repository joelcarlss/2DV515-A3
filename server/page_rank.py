import glob
import pandas as pd
import numpy as np


def get_data():
	list_of_files = glob.glob('./wikipedia/Links/*/*')  # create the list of file
	df = pd.DataFrame(columns=['name', 'links', 'page_rank', 'link_len'])
	for file_name in list_of_files:
		path = str.split(file_name, '/')
		file = open(file_name).read()
		file = file.replace('/wiki/', '')
		array = file.split('\n')[:-1]
		df = df.append({'name': path[4], 'links': array, 'page_rank': 1.0, 'link_len': len(array)}, ignore_index=True)
		# TODO: MAKE THIS A (LIST?) with sets SET!!
	return df


def calculate_page_rank(df, iterations):
	print('start calc')
	i = 0
	while iterations > i:
		for index, row in df.iterrows(): # index makes the row readable in right direction. how?!
			#linking_pages = df[pd.DataFrame(df['links'].tolist()).isin([row['name']]).any(1)]  # Writes out all docs that contains current name
			#pr = (linking_pages['page_rank'] / linking_pages['link_len']) # TODO: Kolla att det inte finns dokument med samma namn i olika filerls
			pr = np.array([7, 9])
			page_rank = 0.85 * pr.sum() + 0.15
			df.loc[index, 'page_rank'] = page_rank  # TODO: These three lines can be a one liner
		i += 1
		print('Iteration: ', i, '/', iterations)
	return df


def read_and_save_data():
	df = get_data()
	result = calculate_page_rank(df, 20)
	# TODO: normalize!
	# result.to_pickle('pagerank.pkl')  # where to save it, usually as a .pkl


read_and_save_data()
