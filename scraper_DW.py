#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


response = requests.get('https://www.dw.com/ru/%D1%82%D0%B5%D0%BC%D1%8B-%D0%B4%D0%BD%D1%8F/s-9119')
doc = BeautifulSoup(response.text, 'html.parser')


# In[3]:


rows = []


# In[4]:


firstnews = doc.select(".carouselTeaser")


# In[5]:


for veryfirst in firstnews:
    print('----------')
    print (veryfirst.text.strip())
    row = {}
    row['cover'] = veryfirst.text.strip()
    rows.append(row)


# In[6]:


news = doc.select(".news")


# In[7]:


for new in news:
    print('----------')
    row = {}
    print (new.text.strip())
    row['current'] = new.text.strip()
    rows.append(row)


# In[8]:


print(rows)


# In[9]:


import pandas as pd


# In[10]:


df = pd.DataFrame(rows)


# In[11]:


df


# In[12]:


df.to_csv("dw_rus_website.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




