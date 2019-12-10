from utils import *


# calculates Word frequency AND location-score
# Takes integers
def calc_scores(docs, words):
	freq = np.zeros(len(docs))
	loc_score = np.zeros(len(docs))
	for i, doc in enumerate(docs):
		for word in words:
			word_at_index = np.where(doc[0] == word)[0] # list of indexes that contains the current word
			freq[i] += len(word_at_index)
			if len(word_at_index) > 0: # This can't happen!!
				loc_score[i] += (word_at_index[0] + 1)
			else:
				loc_score[i] += 100000
	return freq, loc_score


# Make score between 0-1
def normalize(score, small_is_better):
	if small_is_better:
		return score.min() / score
	else:
		return score / score.max()


def run(words):
	word_index = words_to_index(words)  # Gets the index value for the right word, if exeists
	if len(word_index) < 1:  # If no word is found in dictionary
		return 'No results'

	relevant_docs = np.array(get_all_occurrences(word_index))  # All docs that has one or more of the search words

	w_freq, loc_score = calc_scores(relevant_docs, word_index) # Both word frequency and location score
	loc_score = normalize(loc_score, True)  # makes values between 0-1 (Lower is higher)
	w_freq = normalize(w_freq, False)
	page_rank = relevant_docs[:, 5]  # The index place where page_rank exists
	loc_score = loc_score * 0.8
	page_rank = page_rank * 0.5
	score = w_freq + loc_score + page_rank # Adds all the arrays together

	# Puts together all data of interest. Each object in zip is an equal array,
	result = np.array(list(zip(score, relevant_docs[:,1], w_freq, loc_score, page_rank, relevant_docs[:, 2])))
	result = result[result[:, 0].argsort()][::-1][:5]  # Sorts array and reverses it, takes 5 first
	return result_to_object(result)  # Returns named object of the array above

