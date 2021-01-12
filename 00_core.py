#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# default_exp core


# # module core
# 
# > Everything about core.

# In[2]:


#hide
from nbdev.showdoc import *


# In[8]:


#export
def say_hello(to):
    "Say hello to somebody"
    return f'Hello {to}!'


# We can use this to say hello to anyone

# ## example

# In[6]:


say_hello("Sylvain")


# ## test

# In[7]:


assert say_hello("Jeremy")=="Hello Jeremy!"


# # HelloSayer class

# By using `#exports` with an s, this will be exported both in lib and docs.

# In[21]:


#exports
class HelloSayer:
    "Say hello to `to` using `say_hello`"
    def __init__(self, to): self.to = to

    def say(self):
        """
        Do the saying, and it can be a very long proper docstring
        """
        return say_hello(self.to)

    def say_emphasis(self, emphasis):
        """
        Do the saying, and add other things too
        Input:
        emphasis: String
        Output:String
        
        """
        return say_hello(self.to+emphasis)


# By calling show_doc, this will be in the documentation

# In[22]:


show_doc(HelloSayer.say)


# In[23]:


show_doc(HelloSayer.say_emphasis)


# ## example

# In[27]:


o = HelloSayer("Alexis")
o.say()


# In[29]:


o.say_emphasis('!!!')


# # export nbdev
# 
# (not for the documentation, to see if it can be hidden somehow)

# In[25]:


#hide
from nbdev.export import notebook2script; notebook2script()


# In[ ]:




