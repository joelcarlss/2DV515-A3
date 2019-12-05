from utils import *

word = 'george'
data_frame, dictionary = get_data()



# Return all documents including word
def get_all_ocurrences(word):
	word_index = dictionary[word]
	print(word_index)


print(get_all_ocurrences(word))
