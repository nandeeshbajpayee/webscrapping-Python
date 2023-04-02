import pandas as pd
import requests
from bs4 import BeautifulSoup
path = "D:\webscrapping\colleges.csv"
df = pd.read_csv(path)
URLs = list(df.website)

for URL in URLs:

    page = requests.get(URL)
    if (page.status_code == 200):
        print("got")
        soup = BeautifulSoup(page.content, 'html.parser')
        adr = soup.findAll(attrs={'class': 'adr'})
        address = adr[0].text
        print(address)
    data = [[URL]]

df = pd.DataFrame(data, columns=['URLS', 'address'])
df.to_csv('pagedata.csv')
