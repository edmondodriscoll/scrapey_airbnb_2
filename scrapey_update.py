#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd


# In[90]:


import datetime
datetime_object = datetime.datetime.now()
# print(datetime_object)


# In[91]:


import random
list =[]
for x in range(1):
    y= random.randint(1,3)
    list.append(y)


# In[92]:


df = pd.DataFrame(list, columns = ["test"])


# In[93]:


from datetime import datetime, timedelta
n= datetime.strftime(datetime.now() + timedelta(random.randint(0,2)), '%Y-%m-%d')


# In[94]:


n


# In[95]:


df.to_csv("update{}".format(n))


# In[ ]:


print("ran to the end")


# In[ ]:




