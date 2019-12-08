from utils import *


# calculates Word frequency AND location-score
# Takes integers
def calc_scores(docs, words):
	freq = np.zeros(len(docs))
	loc_score = np.zeros(len(docs))
	i = 0
	for doc in docs:
		for word in words:
			word_at_index = np.where(doc[0] == word)[0] # list of indexes that contains the current word
			freq[i] += len(word_at_index)
			if len(word_at_index) > 0:
				loc_score[i] += (word_at_index[0] + 1)
			else:
				loc_score[i] += 100000
		i += 1
	return freq, loc_score


# Make score between 0-1
def normalize(score, small_is_better):
	if small_is_better:
		return score.min() / score
	else:
		return score / score.max()


def run():
	words = ['super', 'mario']
	word_index = words_to_index(words)
	if len(word_index) < 1:
		return 'No results'

	relevant_docs = np.array(get_all_occurrences(word_index))

	w_freq, loc_score = calc_scores(relevant_docs, word_index)
	loc_score = normalize(loc_score, True)  # makes values between 0-1 (Lower is higher)
	w_freq = normalize(w_freq, False)
	score = w_freq + 0.8 * loc_score

	result = np.array(list(zip(score, relevant_docs[:,1], w_freq, loc_score)))
	print(result[result[:, 0].argsort()][::-1][:5]) # Sorts array and reverses it, takes 5 first


run()
