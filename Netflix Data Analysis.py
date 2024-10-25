#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r"C:\Users\vivek.kumar131\Downloads\8. Netflix Dataset.csv")


# In[3]:


data


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.shape       #to show the no. of Rows and columns


# In[8]:


data.size


# In[10]:


data.columns


# In[11]:


data.dtypes


# In[12]:


data.info()  # To show index columns, data-type of each columns, memory at once


# In[13]:


data.head()


# In[14]:


data.shape


# In[15]:


data.duplicated()    # check the duplicat row 


# In[21]:


data[data.duplicated()] # To check row and detect the Duplicat row


# In[22]:


data.drop_duplicates(inplace =True)              # To Remove the Duplicate rows permanently


# In[23]:


data[data.duplicated()]


# In[24]:


data.shape


# # Task2 : Is there any Null Value present in any column ?show with Heat-map.

# In[25]:


data.head()


# In[26]:


data.isnull()


# In[27]:


data.isnull().sum()  # To Show the count of null values


# Seaborn library(heat-map)

# In[31]:


import seaborn  as sns


# In[32]:


sns.heatmap(data.isnull())                # using heat-map to show null values count


# In[37]:


data.head()


# In[41]:


data[data['Title'].isin(['House of cards'])]   # to show records of particular itam is any column


# In[39]:


data.head()


# In[42]:


data[data['Title'].str.contains('House of cards')]


# # Q > In which year heighest number of tv shows & movies were released? show Bar graph

# In[45]:


data.dtypes


# In[47]:


data['Data_N'] =pd.to_datetime(data['Release_Date'])


# In[48]:


data.head()


# In[ ]:





# In[49]:


data.dtypes


# In[52]:


data['Data_N'].dt.year.value_counts()


# In[53]:


data['Data_N'].dt.year.value_counts().plot(kind='bar')


# # How many Movie & TV shows in dataset

# In[55]:


data.head(2)


# In[61]:


data.groupby('Category').Category.count()


# In[62]:


sns.countplot(data['Category'])


# # Q>Show all the movies that were released in year 2000. 

# In[63]:


data.head()


# In[65]:


data['Year']= data['Data_N'].dt.year


# In[67]:


data.head()


# In[72]:


#Filtering
data[(data['Category'] =='Movie') & (data['Year']==2000)]


# In[73]:


data[(data['Category'] =='Movie') & (data['Year']==2020)]


# # Shows only the Title of all TV shows that were released in india only.

# In[74]:


data.head()


# In[92]:


data = data[(data['Category']=='TV Show') & (data['Country']=='India')]


# In[93]:


data


# # Q7 > Show the Top Directors, who gave the heighest number of TV shows & Movies to Netflix ?

# In[97]:


# data['Director'].value_counts().head(1)
data.head(2)


# In[98]:


data['Director'].value_counts()


# In[99]:


from sklearn.datasets import load_boston


# In[ ]:





# In[ ]:





# In[ ]:




