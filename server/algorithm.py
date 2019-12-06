from utils import *

words = ['academic', 'study']
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
		if any(item in index_list for item in a[0]):
			result.append(a)

	return result


def run():
	word_index = words_to_index(words)
	if len(word_index) < 1:
		return 'No results'

	relevant_docs = get_all_occurrences(word_index)
	# print(relevant_docs)
	print(len(relevant_docs))

run()