import numpy as np

def get_data(source = 'blogdata.txt'):
    # Create numpy array data from blogdata.txt
    blog_names = np.genfromtxt(source, delimiter='\t', usecols=0, dtype=str)[1:] # Names of all blogs(column 0 in doc)
    blog_data = np.genfromtxt(source, delimiter='\t', skip_header=1)[:, 1:] # Each blogs word freq. (rows in doc)
    # named_data = {label: row for label, row in zip(blog_names, blog_data)}  # Pretty presentation (Blog name then word-freq)
    return blog_data, blog_names


def elements_for_names(index_list, names):
    name_list = []
    for key in index_list:
        name_list.append(list(names[index_list[key]]))

    return name_list
