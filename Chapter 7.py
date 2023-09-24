#!/usr/bin/env python
# coding: utf-8

# In[4]:


stuff = 'Hello\n World!'
stuff


# In[6]:


print(stuff)


# In[7]:


stuff = 'X\nY'


# In[8]:


print(stuff)


# In[9]:


len(stuff)


# In[1]:


xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)


# In[2]:


fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)


# In[4]:


fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))


# In[5]:


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From:') :
        continue
    print(line)


# In[6]:


fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)


# In[ ]:




