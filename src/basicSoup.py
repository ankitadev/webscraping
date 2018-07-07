import pandas as pd
import requests
from bs4 import BeautifulSoup
res = requests.get("----------URL----------------")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))
