#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd


# In[63]:


import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)


# In[44]:


import random
list =[]
for x in range(1):
    y= random.randint(1,3)
    list.append(y)


# In[47]:


df = pd.DataFrame(list, columns = ["test"])


# In[86]:


from datetime import datetime, timedelta
n= datetime.strftime(datetime.now() + timedelta(random.randint(0,2)), '%Y-%m-%d')


# In[87]:


df.to_csv("test{}".format(n))


# In[ ]:





# In[ ]:




