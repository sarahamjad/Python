#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')


# In[8]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')

z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')


# In[10]:


greet = 'Hello Bob'
print(len(greet))


# In[11]:


x = [ 1, 2, 'joe', 99]
print(len(x))


# In[12]:


print(range(4))
[0, 1, 2, 3]
friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))
print(range(len(friends)))
[0, 1, 2]


# In[14]:


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)


# In[15]:


friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends)
print(friends[1])


# In[23]:


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
if not line.startswith('From ') :
    words = line.split()
print(words[2])


# In[25]:


print(pieces[1])


# In[ ]:





# In[ ]:




