#!/usr/bin/env python
# coding: utf-8

# In[120]:


import requests
from bs4 import BeautifulSoup
# Import pandas library
import pandas as pd

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://scirp.org/journal/articles.aspx?searchcode=malawi&searchfield=All&page=1&skid=60353140'
src = requests.get(url,headers,timeout=3, verify=False ).text

soup = BeautifulSoup(src, 'lxml')
data = soup.find('ul', attrs={'class': 'list-unstyled list_link'})
publications = data.find_all('li')
def single_book(li_data):
    title = li_data.find('div',attrs={'class': 'list_t'}).find('a').text
    author = li_data.find('div',attrs={'class': 'txt5'}).find('a').text
    year = li_data.find('div',attrs={'class': 'list_unit'}).text
    journal = li_data.find('div',attrs={'class': 'list_unit'}).find_all('a')
    jop = journal[0].text
    vol = journal[1].text
    year_space_str = year.strip()
    year = year_space_str[len(jop)+len(vol)+1:]
    doi = li_data.find('div',attrs={'class': 'list_doi'}).find('a').text
    return {'Title':title, 'Author':author, 'Year':year, 'Journal Of Publication':jop, 'volume':vol, 
            'Year':year, 'DOI':doi }

if __name__ == "__main__":
    data_list = []
    for publication in publications:
        data_list.append(single_book(publication))
    data_frame = pd.DataFrame.from_dict(data_list)
    data_frame.to_csv("publications.csv")


# In[108]:





# In[114]:





# In[115]:





# In[ ]:




