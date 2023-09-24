#!/usr/bin/env python
# coding: utf-8

# In[1]:


purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)


# In[2]:


ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)

ddd['age'] = 23
print(ddd)


# In[4]:


ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)
ddd['age'] = 23
print(ddd)


# In[5]:


ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)


# In[6]:


counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('Words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
print('Counts', counts)


# In[7]:


jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(list(jjj))

print(jjj.keys())

print(jjj.values())
[100, 1, 42]
print(jjj.items())


# In[ ]:




