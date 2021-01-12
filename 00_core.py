#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# default_exp core


# # module name here
# 
# > API details.

# In[2]:


#hide
from nbdev.showdoc import *


# In[8]:


#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'


# We can use this to say hello to anyone

# In[6]:


say_hello("Sylvain")


# In[7]:


assert say_hello("Jeremy")=="Hello Jeremy!"


# In[ ]:




