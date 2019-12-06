import glob
import pandas as pd


def get_data():
	list_of_files = glob.glob('./wikipedia/Links/*/*')  # create the list of file
	df = pd.DataFrame(columns=['name', 'links'])
	for file_name in list_of_files:
		path = str.split(file_name, '/')
		file = open(file_name).read()
		file = file.replace('/wiki/', '')
		array = pd.Index(file.split('\n')[:-1])
		df = df.append({'name': path[4], 'links': array}, ignore_index=True)
	# length links arr at index 0
	# print(len(df.iloc[0]['links']))
	return df

def calculate_page_rank():
	test = 'Computer_scientist'
	df = get_data()
	print(df['name'])
	# https://stackoverflow.com/questions/53342715/pandas-dataframe-select-rows-where-a-list-column-contains-any-of-a-list-of-strin
	print(df[pd.DataFrame(df['links'].tolist()).isin([test]).any(1)])



calculate_page_rank()
