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


# # HelloSayer class

# In[10]:


#exports
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to

    def say(self):
        "Do the saying"
        return say_hello(self.to)


# In[11]:


show_doc(HelloSayer.say)


# In[12]:




o = HelloSayer("Alexis")
o.say()


# In[ ]:




