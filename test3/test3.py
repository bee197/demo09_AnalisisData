import json

import pandas as pd
import requests

url = 'https://quotes.toscrape.com/api/quotes?page=1'
res = requests.get(url)
data = res.json() # 获取该页的quotes数据
print(data)

df_quotes = pd.DataFrame(data['quotes'], columns=['text'])
df_authors = pd.DataFrame(data['quotes'], columns=['author'])

df_quotes.to_csv('quotes.csv', index=False)
df_authors.to_csv('authors.csv', index=False)
