import numpy as np
import re
import pandas as pd

def get_data(source = 'wikipedia_300/wikipedia_300.csv'):
    df = pd.read_csv(source)
    # Each stringed Text becomes array of words.
    text = df['Text'].str.replace('.', '')
    words = text.str.split(' |\n')  # Splits default value = whitespace
    return df, words


# create dictionary of index
def dictionary(collections):
    dict = {}
    for text in collections:
        for word in text:
            if word not in dict:
                dict[word] = len(dict)


    print('done')
    return dict


def dictionaty_two(d_frame):
    empty_df = pd.DataFrame(columns=['Text', 'Category'])
    empty_df = empty_df.append({'Text': d_frame[0], 'Category': 'Test'}, ignore_index=True) # TODO: This might be it
    # TODO: iterate and append lists as ints instead of words
    print(empty_df)


data, words = get_data()
dictionaty_two(words)
