import glob
import pandas as pd
import numpy as np


def get_data():
	list_of_files = glob.glob('./wikipedia/Links/*/*')  # create the list of file
	df = pd.DataFrame(columns=['name', 'links'])
	for file_name in list_of_files:
		path = str.split(file_name, '/')
		file = open(file_name).read()
		file = file.replace('/wiki/', '')
		array = file.split('\n')[:-1]
		df = df.append({'name': path[4], 'links': array, 'page_rank': 1, 'link_len': len(array)}, ignore_index=True)
	# length links arr at index 0
	# print(len(df.iloc[0]['links']))
	return df


def calculate_page_rank(df, iterations):
	test = 'Computer_scientist'
	i = 0
	while iterations > i:
		for index, row in df.iterrows(): # index makes the row readable in right direction. how?!
			# https://stackoverflow.com/questions/53342715/pandas-dataframe-select-rows-where-a-list-column-contains-any-of-a-list-of-strin
			linking_pages = df[pd.DataFrame(df['links'].tolist()).isin([row['name']]).any(1)]  # Writes out all docs that contains test
			pr = linking_pages['page_rank'] / linking_pages['link_len']
			page_rank = 0.85 * pr.sum() + 0.15
			df.loc[index, 'page_rank'] = page_rank #  TODO: These three lines can be a oneliner


			# TODO: Make it run 20 times then save it to DB
		i += 1
		print('Iteration: ', i, '/', iterations)
	return df


def read_and_save_data():
	df = get_data()
	result = calculate_page_rank(df, 20)
	result.to_pickle('pagerank.pkl')  # where to save it, usually as a .pkl


read_and_save_data()
