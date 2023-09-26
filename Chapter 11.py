#!/usr/bin/env python
# coding: utf-8

# In[4]:


class Apple: 
    pass 
class Apple: 
    color =" "
    Flavor= " " 
jonagold = Apple() 
jonagold.color = " red" 
jonagold. flavor = "sweet" 
print(jonagold . color) 
print(jonagold . flavor)  


# In[5]:


class Apple: 
	pass 
class Apple: 
	Color="" 
	flavor ='"' 
jonagold =Apple() 
jonagold.color= "red" 
jonagold. flavor ="sweet" 
print(jonagold . color) 
print(jonagold . flavor) 
 
print(jonagold.color.upper()) 


# In[8]:


class Flower: 
	color =' unknown ' 
rose= Flower() 
rose. color =" red"  
violet = Flower()
violet. color ="blue" 

this_pun_is_for_you ="Sugar is sweet, and so are you. " 
print("Roses are {}," . format(rose.color)) 
print("violets are {}," . format(violet.color)) 
print ( this_pun_is_for_you)


# In[16]:


class Cat: 
	Name="" 
	def speak(self) : 
		print( "Meow! I'm {}! Meow" .format(self.name)) 
myLuna =Cat()  
myLuna.name ="Luna"
myLuna.speak() 

myBella =Cat() 
myBella.name="Bella" 
myBella.speak() 


# In[34]:


class Apple: 
    def __init__(self, color, flavor):
        self.color =color 
        self.flavor =flavor 
jonagold = Apple("red","sweet") 
print (jonagold.color)


# In[69]:


class Animal: 
	sound =""
def __init__(self, name) : 
        self.name= name 
def speak(self): 
		Print("{sound} I'm {name}!  (sound)" .format(name=self.name, sound=self.sound) ) 
class Cat(Animal): 
    sound  = "Meow!"
myLuna=Cat("Luna") 
myLuna.speak( ) 

class Cow(AnimaI) : 
	sound ="Moooo" 
myCow =Cow("Milky")
myCow. speak( ) 


# In[71]:


class Repository: 
    def __init__( self) : 
        self. packages ={}
    def add_package(self, package) : 
        self. packages [package. name] = package 
    def total_size(self): 
        result = 0
        for package in self. packages.values(): 
            result +=  package. size 
        return result 


# In[ ]:




