import glob
import pandas as pd


def get_data():
	list_of_files = glob.glob('./wikipedia/Links/*/*')  # create the list of file
	df = pd.DataFrame(columns=['name', 'links'])
	for file_name in list_of_files:
		path = str.split(file_name, '/')
		file = open(file_name).read()
		file = file.replace('/wiki/', '')
		array = file.split('\n')[:-1]
		df = df.append({'name': path[4], 'links': array, 'page_rank': 1}, ignore_index=True)
	# length links arr at index 0
	# print(len(df.iloc[0]['links']))
	return df


def calculate_page_rank():
	test = 'Computer_scientist'
	df = get_data()
	# https://stackoverflow.com/questions/53342715/pandas-dataframe-select-rows-where-a-list-column-contains-any-of-a-list-of-strin
	# print(df[pd.DataFrame(df['links'].tolist()).isin([test]).any(1)]) # Writes out all docs that contains test
	for index, row in df.iterrows(): # index makes the row readable in right direction. how?!
		links = df[pd.DataFrame(df['links'].tolist()).isin([row['name']]).any(1)]  # Writes out all docs that contains test
		#  print(len(links))
		#  print()
		iterate_page_rank(links)

		break


def iterate_page_rank(linked_docs):
	for index, link_row in linked_docs.iterrows():
		print(link_row)


calculate_page_rank()
