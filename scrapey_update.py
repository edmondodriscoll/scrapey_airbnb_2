#!/usr/bin/env python
# coding: utf-8

# In[13]:


import datetime


# In[16]:


import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)


# In[18]:


import os 


# In[22]:



os.system('touch today1' )




# In[44]:


import random
list =[]
for x in range(1):
    y= random.randint(1,3)
    list.append(y)
    print(random.randint(1,3))


# In[45]:


list


# In[46]:


import pandas as pd


# In[47]:


df = pd.DataFrame(list, columns = ["test"])


# In[48]:


df


# In[49]:


df.to_csv("test.csv")


# In[ ]:




