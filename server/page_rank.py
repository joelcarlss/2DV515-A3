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


def calculate_page_rank():
	test = 'Computer_scientist'
	df = get_data()

	for index, row in df.iterrows(): # index makes the row readable in right direction. how?!
		# https://stackoverflow.com/questions/53342715/pandas-dataframe-select-rows-where-a-list-column-contains-any-of-a-list-of-strin
		linking_pages = df[pd.DataFrame(df['links'].tolist()).isin([row['name']]).any(1)]  # Writes out all docs that contains test
		pr = linking_pages['page_rank'] / linking_pages['link_len']
		page_rank = 0.85 * pr.sum() + 0.15
		df.loc[index, 'page_rank'] = page_rank


		# TODO: Make it run 20 times then save it to DB



calculate_page_rank()
