import glob
import pandas as pd
import numpy as np


def get_data():
	list_of_files = glob.glob('./wikipedia/Links/*/*')  # create the list of file
	datalist = []
	for file_name in list_of_files:
		path = str.split(file_name, '/')
		file = open(file_name).read()
		file = file.replace('/wiki/', '')
		array = file.split('\n')[:-1]
		s = set(array)
		datalist.append({'name': path[4], 'links': s, 'page_rank': 1.0})
		# TODO: MAKE THIS A (LIST?) with sets SET!!
	return datalist


def calculate_page_rank(datalist, iterations):
	print('start calc')
	i = 0
	while iterations > i:
		for page in datalist: # index makes the row readable in right direction. how?!
			pr = 0
			for p in datalist:
				if page['name'] in p['links']:
					pr += p['page_rank'] / len(p['links'])
			page['page_rank'] = (0.85 * pr + 0.15)

		i += 1
		print('Iteration: ', i, '/', iterations)
	return datalist

def normalize(result):
	# test = result.to_numpy()
	print(len(result))
	m = 0
	for obj in result:
		if obj['page_rank'] > m:
			m = obj['page_rank']

	print(m)
	for i, obj in enumerate(result):
		result[i]['page_rank'] = (obj['page_rank'] / m)
	return result


def read_and_save_data():
	data_list = get_data()
	result = calculate_page_rank(data_list, 20)
	result = normalize(result)
	result = pd.DataFrame(result)

	result.to_pickle('pagerank.pkl')  # where to save it


read_and_save_data()
