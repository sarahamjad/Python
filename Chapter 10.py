#!/usr/bin/env python
# coding: utf-8

# In[1]:


x = ('Glenn', 'Sally', 'Joseph')
print(x[2])

y = ( 1, 9, 2 )
print(y)

print(max(y))


# In[2]:


(x, y) = (4, 'fred')
print(y)

(a, b) = (99, 98)
print(a)


# In[6]:


d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print(k, v)

tups = d.items()
print(tups)


# In[8]:


fhand = open('romeo.txt')
counts = {}
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0 ) + 1
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)


# In[ ]:




