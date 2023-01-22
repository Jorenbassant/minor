#!/usr/bin/env python
# coding: utf-8

# ## Assignment BDD Sprint 2 week 1 Joren

# Data cleaning:

# In[20]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

survey = pd.read_csv("survey.csv")
survey.head()


# In[21]:


steps = pd.read_csv("steps.csv", sep=";")
steps.head()


# >> I imported all the necessities, and both csv's. I then assigned the ; to be the seperator in the Steps-file, in order to merge them. I then scanned both top rows of the data

# In[22]:


mergeddf = pd.merge(steps, survey, on = "id")
mergeddf.head()


# >> I merged both csv files into one, based on the common column 'id'

# In[23]:


mergeddf['weight'].value_counts() 


# >> By using this code I check all the value frequencies of the column 'weights'. I now see that there are impossible values such as 700 kilo and 6 kilo. If I remove those, I improve the final visualizations.

# In[24]:


def cut_off(x):
    if (x > 250.0 or x < 35.0): 
        return float('NaN')
    else: 
        return x
    
mergeddf['weight'] = mergeddf['weight'].apply(cut_off)
mergeddf.head()


# >> By using this code I removed all the impossible weight values past 250 kilo and under 35 kilo

# In[25]:


mergeddf['MeanSteps'] = mergeddf.loc[:,'13-5-2014':].mean(axis=1).round(0)
mergeddf.head()


# >> I wanted to calculate the mean steps, but I think that the MeanSteps is calculating the NaN's as well, because the numbers are very low.

# In[26]:


sns.distplot(mergeddf['MeanSteps'].dropna(), kde=False)
plt.title('Mean steps')
plt.xlabel('Mean steps')
plt.show()


# >> I created the plot

# Exploratory data analysis:
# 

# In[27]:


sns.violinplot(mergeddf['MeanSteps'])
sns.swarmplot(mergeddf['MeanSteps'], color='red')
plt.show()


# In[28]:


mergeddf.describe()


# >> Here I created the Summary statistics

# In[ ]:





# In[ ]:




