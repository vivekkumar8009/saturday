#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('Algerian_forest_fires_cleaned.csv')


# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.head()


# In[6]:


#drop mont, day and year
df.drop(['day','month','year'],axis=1,inplace=True)


# In[7]:


df.head()


# In[8]:


df['Classes'].value_counts()


# In[9]:


## Cncoding
df['Classes']=np.where(df['Classes'].str.contains("not fire"),0,1)


# In[10]:


df.head()


# In[11]:


df.tail()


# In[12]:


df['Classes'].value_counts()


# In[13]:


## Independed and depended feature
X =df.drop('FWI', axis=1)
y=df['FWI']


# In[15]:


X.head()


# In[16]:


y.head()


# In[19]:


## Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.25,random_state=42)


# In[20]:


X_train.shape,X_test.shape


# In[21]:


## Feature selection on corellation
X_train.corr()


# In[22]:


## Check for multicollinearity
plt.figure(figsize=(12,10))
corr = X_train.corr()
sns.heatmap(corr,annot=True)


# In[34]:


def correlation(dataset,threshold):
    col_corr = set()
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold:
                colname = corr_matrix.columns[i]
                col_corr.add(colname)
        return col_corr      


# In[35]:


correlation(X_train,0.85)


# In[36]:


correlation(X_train,0.70)


# # Feature Scaling or Standardization 

# In[38]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# In[39]:


X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled =scaler.transform(X_test)


# In[40]:


X_train_scaled


# # Box plots To understand effect of Standard

# In[41]:


plt.subplots(figsize=(15,5))
plt.subplot(1,2,1)
sns.boxplot(data=X_train)
plt.title('X_train before Scalling')
plt.subplot(1,2,2)
sns.boxplot(data= X_train_scaled)
plt.title('X_train after Scaling')


# # Linear Regression Model

# In[55]:


from sklearn.linear_model import LinearRegression

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
linreg = LinearRegression


# In[62]:


linreg.fit(X_train_scaled,y_train)
y_pred = linreg.predict(X_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 score", score)
plt.scatter(y_test,y_pred)


# # Lasso regression Model

# In[63]:


from sklearn.linear_model import Lasso

from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
lasso = Lasso()
lasso.fit(X_train_scaled,y_train)
y_pred = Lasso.predict(X_test_scaled)
mae = mean_absolute_error(y_test,y_pred)
score = r2_score(y_test,y_pred)
print("Mean absolute error", mae)
print("R2 score", score)
plt.scatter(y_test,y_pred)


# In[64]:


from sklearn.linear_model import Lasso
from sklearn.metrics import r2_score, mean_absolute_error

lasso = Lasso()
lasso.fit(X_train_scaled, y_train)
y_pred = lasso.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred)
score = r2_score(y_test, y_pred)

print('Mean absolute error:', mae)
print('R2 score:', score)

plt.scatter(y_test, y_pred, label='Predicted vs. Actual')
plt.xlabel('Actual target value')
plt.ylabel('Predicted target value')
plt.title('Lasso regression on test data')
plt.legend()
plt.show()


# In[ ]:




