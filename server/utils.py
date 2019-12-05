import pandas as pd
import numpy as np
from db import *
import glob


def save_to_db(df):
	sql = "INSERT INTO text (name, category, text) VALUES (%s, %s, %s)"
	# val = (name, category, text)
	# mycursor.execute(sql, val)
	df.to_sql(df, mydb)


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
		break
	return df, dict



data_frame, dictionary = get_data()

print(data_frame)
