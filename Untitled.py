#!/usr/bin/env python
# coding: utf-8

# In[5]:


N =1000
X = 12
Y =12234
T = 12


# In[6]:


a = "mpiexec -np " + str(N) + " ./scale.out -nx " + str(X) + " -ny " + str(Y) + " -nt " + str(T)

print(a)
# In[ ]:




