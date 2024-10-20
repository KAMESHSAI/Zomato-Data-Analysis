#!/usr/bin/env python
# coding: utf-8

# # ZOMATO DATA ANALYSIS PROJECT

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # creating data Frame

# In[3]:


dataframe=pd.read_csv("Zomato data .csv")


# In[4]:


print(dataframe)


# # CHECKING VALUES OF DATASET

# In[12]:


dataframe.info()


# # DATA CLEANING 

# In[11]:


#converting The data Type of column- "rate"

def handleRate(value):
    value=str(value).split('/')
    value=value[0];
    return float(value)

dataframe['rate']=dataframe['rate'].apply(handleRate)
print(dataframe.head())


# # CHECKING TYPES OF RESTAURANTS 

# In[14]:


dataframe.head()


# # VISUALIZING TYPE OF RESTURENTS USING SEABORN

# In[16]:


sns.countplot(x=dataframe['listed_in(type)'])
plt.xlabel("type of resturant")


# # INSIGHT= Majority Types of resturents are "Dinning"

# In[17]:


#analysis 2


# # Which Restaurant type recieved majority votes from the Customers

# In[21]:


grouped_data=dataframe.groupby('listed_in(type)')['votes'].sum()
result=pd.DataFrame({'votes':grouped_data})
plt.plot(result,c="green",marker="o")
plt.xlabel("Types of Restaurent",c="red",size=20)
plt.ylabel("votes",c="black",size=20)


# # INSIGHT- Dinning Resturants has received maximum Votes

# In[22]:


#majority Rating recieved
   


# In[25]:


plt.hist(dataframe['rate'],bins=15)
plt.title("Ratings Distribution")
plt.show()


# # INSIGHT- The majority ratings Received is from 3.5 - 4

# In[26]:


#Average order Spending by Couples


# In[27]:


dataframe.head()


# In[28]:


couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # INSIGHT= Majority cost by couples Orders is Rs:300

# In[29]:


#which mode recieves maximum Rating


# In[30]:


dataframe.head()


# In[33]:


plt.figure(figsize=(6,6))
sns.boxplot(x='online_order', y='rate',data=dataframe)


# # INSIGHT= Online Order Recived higher Rating compared to online orders 

# In[ ]:




