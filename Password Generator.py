#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import string


# In[ ]:


print("Welcome to random password generator")
def fun():
    

    length = int(input("enter the length of password you want :- "))
    lowerC = string.ascii_lowercase
    upperC = string.ascii_uppercase
    digitC = string.digits
    symbolsC = string.punctuation
    combine = lowerC+upperC+digitC+symbolsC
    x = random.sample(combine,length)
    password = "".join(x)
    print(password)

    fun()
fun()


# In[ ]:




