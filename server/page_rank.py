import glob
import pandas as pd
import numpy as np


def get_data():
	list_of_files = glob.glob('./wikipedia/Links/*/*')  # create the list of file
	datalist = []
	for file_name in list_of_files:
		name = str.split(file_name, '/')[4]
		file = open(file_name).read()
		file = file.replace('/wiki/', '')
		s = set(file.split('\n')[:-1])
		datalist.append({'name': name, 'links': s, 'page_rank': 1.0})
	return datalist


def calculate_page_rank(datalist, iterations):
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
	m = max(obj['page_rank'] for obj in result)
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
