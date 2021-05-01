import pandas as pd

data = pd.read_csv('horoscopes.csv', header = None, delimiter = '|').dropna()
texts = data[1]

with open('train.txt', 'w') as f:
  f.write('\n'.join(texts[:12500]))

with open('valid.txt', 'w') as f:
  f.write('\n'.join(texts[12500:]))
