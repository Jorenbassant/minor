#!/usr/bin/env python
# coding: utf-8

# after checking the different data files, I chose Gender recognition of voice. I'm curious what I can visualize from within these different frequencies.

# ## Data cleaning

# In[10]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("voice.csv")
df.head()


# In[11]:


df_nieuw = df[["meanfreq", "sd", "median", "Q25", "Q75", "IQR", "skew", "label"]]
df_nieuw.head()


# I stripped it down to eight variables

# In[8]:


def above_0.3(x):
    if(x > 0.3): 
        return float('0')
    else: 
        return x
df_nieuw['Q25'] = df_nieuw['Q25'].apply(above_.3)


# I removed all the numbers above 0.3

# In[9]:


sns.histplot(df_nieuw['Q25'].dropna(), kde=False)
plt.title('Q25')
plt.xlabel("Q25")
plt.show()


# I created the visualisation

# ## Exploratory data analysis

# In[13]:


df_nieuw['meanfreq'].name = 'Count (frequency)' #Here I created a new mean variable
file_size = df_nieuw['meanfreq'].dropna() #removing the NA's
sns.distplot(file_size, kde=False) 

mean_size = df_nieuw['meanfreq'].mean()
median_size = df_nieuw['meanfreq'].median()

print(f'The median filesize is: {median_size} Frequency')
print(f'The mean filesize is: {mean_size} Frequency')

sns.distplot(file_size, kde=False)
plt.title('Mean of frequency')
plt.axvline(median_size, 0, 600, color='red', label='median')
plt.axvline(mean_size, 0, 600, color='blue', label='mean') 
plt.legend() #With this I made the legend
plt.show()


# In[ ]:


gender = sns.boxplot(x = 'label', y = 'meanfreq', data = df_nieuw)
sns.set_style("whitegrid")
gender.set_title('Mean of frequency grouped by gender')
gender.set_xlabel('gender')
gender.set_ylabel('mean of frequency')

