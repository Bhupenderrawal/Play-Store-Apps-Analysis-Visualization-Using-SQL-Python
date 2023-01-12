#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

import numpy as np

from numpy import nan

file = pd.read_csv(r"C:\Users\super\Downloads\Playstore project\playstoreliveproj Drive FIle\playstore_reviews.csv", index_col='App')
file


# In[2]:


file = file.dropna()


# In[3]:


len(file)


# In[4]:


file


# In[5]:


file.to_csv("reviews.csv")

