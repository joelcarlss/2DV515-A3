import pandas as pd

# Read CSV file
df = pd.read_csv('wikipedia_300/wikipedia_300.csv')

# all rows where Category == Games
df[df['Category'] == 'Games']


# all texts where Category == Games
result = df['Text'][df['Category'] == 'Games']



print(result)
