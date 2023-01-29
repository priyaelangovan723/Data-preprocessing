#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import pandas as pd 
from warnings import filterwarnings
filterwarnings('ignore')
df=pd.read_csv("https://datahack-prod.s3.amazonaws.com/train_file/train_v9rqX0R.csv")
df.head()


# In[7]:


df.describe()


# In[8]:


df.shape()


# In[9]:


df.tail(20)


# In[ ]:


# What is the impact of item weight on sales?
# What is the impact of MRP on sales?
# What is the impact of outlet size on sales?
# What is the impact of item visibility on sales?
# What is the impact of item type on sales?


# In[ ]:


univariate analysis


# In[10]:


df.columns


# In[ ]:


# continous column


# In[38]:


con_col=['Item_Weight','Item_Visibility','Item_MRP','Item_Outlet_Sales']


# In[39]:


import seaborn as sns 


# In[41]:


sns.kdeplot(x=con_col[0],data=df)


# In[42]:


sns.kdeplot(x=con_col[1],data=df)


# In[43]:


sns.kdeplot(x=con_col[2],data=df)


# In[44]:


sns.kdeplot(x=con_col[3],data=df)


# In[45]:


df['Item_Fat_Content'].replace({'low fat':'Low Fat',
                                'LF':'Low Fat',
                               'reg':'Regular'},inplace=True)


# In[49]:


cat_col=['Item_Identifier','Item_Fat_Content','Item_Type','Outlet_Identifier','Outlet_Establishment_Year','Outlet_Size','Outlet_Location_Type','Outlet_Type']


# In[50]:


sns.countplot(x=cat_col[1],data=df)


# In[51]:


sns.countplot(x=cat_col[2],data=df)


# In[52]:


sns.countplot(x=cat_col[3],data=df)


# In[53]:


df


# In[54]:


df['Item_Fat_Content'].replace({'low fat':'Low Fat',
                                'LF':'Low Fat',
                               'reg':'Regular'},inplace=True)


# In[55]:


sns.countplot(x=cat_col[1],data=df)


# In[57]:


import matplotlib.pyplot as plt
plt.figure(figsize=(12,8))
sns.countplot(x=cat_col[2],data=df)
plt.show()


# In[58]:


plt.figure(figsize=(25,10))
sns.countplot(x=cat_col[3],data=df)
plt.show()


# In[ ]:


# Bivariate Analysis


# In[63]:


con_col


# In[ ]:


# con vs con


# In[65]:


sns.scatterplot(x=con_col[1],y='Item_Outlet_Sales',data=df)


# In[67]:


sns.scatterplot(x=con_col[2],y='Item_MRP',data=df)


# In[81]:


sns.scatterplot(x=con_col[2],y='Item_Outlet_Sales',data=df)


# In[82]:


sns.scatterplot(x=con_col[0],y='Item_Outlet_Sales',data=df)


# In[83]:


sns.boxplot(x=con_col[0],y='Item_Outlet_Sales',data=df)


# In[ ]:


sns.boxplot(x=con_col[1],y='Item_Outlet_Sales',data=df)


# In[ ]:


sns.boxplot(x=con_col[0],y='Item_Outlet_Sales',data=df)


# In[85]:


#cat vs con


# In[86]:


sns.boxplot(x=cat_col[0],y='Item_Outlet_Sales',data=df)


# In[87]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[88]:


sns.boxplot(x=cat_col[1],y='Item_Outlet_Sales',data=df)


# In[89]:


sns.boxplot(x=cat_col[4],y='Item_Outlet_Sales',data=df)


# In[7]:


df.isnull().sum()


# In[6]:


df


# In[9]:


df[df['Item_Identifier']=='FDP10']


# In[21]:


null_index=df[df['Item_Weight'].isnull()].index


# In[22]:


for i in null_index:
    itm=df.loc[i,'Item_Identifier']
    val=df[df['Item_Identifier']==itm]['Item_Weight'].mean()
    df.loc[i,'Item_Weight']=val


# In[23]:


df[df['Item_Weight'].isnull()]


# In[15]:


df['Item_Weight'].fillna(df['Item_Weight'].mean(),inplace=True)


# In[16]:


df[df['Item_Weight'].isnull()]


# In[24]:


null_index=df[df['Item_Weight'].isnull()].index


# In[25]:


for i in null_index:
    itm=df.loc[i,'Item_Identifier']
    val=df[df['Item_Identifier']==itm]['Item_Weight'].mode()
    df.loc[i,'Item_Weight']=val


# In[26]:


df['Item_Weight'].fillna(df['Item_Weight'].mode(),inplace=True)


# In[27]:


df[df['Item_Weight'].isnull()]


# In[28]:


null_index=df[df['Item_Weight'].isnull()].index


# In[29]:


for i in null_index:
    itm=df.loci[i,'Item_Identifier']
    val=df[df['Item_Identifier']==itm]['Item_Weight'].mode()
    df.loci[i,'Item_Weight']=val


# In[30]:


df[df['Item_Weight'].isnull()]


# In[32]:


df['Outlet_Size'].fillna(df['Outlet_Size'].mode(),inplace=True)


# In[33]:


df.isnull().sum()


# In[35]:


sns.boxplot(x=con_col[0],data=df)


# In[36]:


import seaborn as sns
import matplotlib.pyplot as plt


# In[39]:


sns.boxplot(x=con_col[0],data=df)


# In[40]:


sns.boxplot(x=con_col[2],data=df)


# In[41]:


sns.boxplot(x=con_col[1],data=df)


# In[43]:


sns.boxplot(x=np.log(df['Item_Outlet_Sales']))


# sns.boxplot(x=np.sqrt(x=np.sqrt(df['Item_

# In[44]:


sns.boxplot(x=np.sqrt(df['Item_Outlet_Sales']))


# In[45]:


df['Item_Type'].unique()


# In[46]:


per=['Dairy', 'Soft Drinks', 'Meat', 'Fruits and Vegetables',
       'Household', 'Baking Goods', 'Snack Foods', 'Frozen Foods',
       'Breakfast', 'Health and Hygiene', 'Hard Drinks', 'Canned',
       'Breads', 'Starchy Foods', 'Others', 'Seafood']
def perishable(x):
    if x in per:
        return 'per'
    else:
        return 'non-per'


# In[48]:


df['Item_Type']=df['Item_Type'].apply(perishable)


# In[49]:


df['Item_Type']


# In[50]:


df['Outlet_Identifier'].unique()


# In[53]:


df['Outlet_Identifier'].value_counts()


# In[55]:


Outlet=['OUT010','OUT019']
def Outlet(x):
    if x in Outlet:
        return 'minor_outlet'
    else:
        return 'major_outlet'
df['Outlet_Identifier']=df['Outlet_Identifier'].apply(Outlet)


# In[56]:


df['Outlet_Identifier']


# In[ ]:




