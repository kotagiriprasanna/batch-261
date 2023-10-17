#!/usr/bin/env python
# coding: utf-8

# In[3]:


### Strings 
* Strings are sequence of characters, enclosed in single quotes (''), double quotes (""),triple-single or triple-quotes (''' ''')
* Triple-quotes are used as multilines strings, multiline comments and as doc strings.
* It is an immutable data type, which means once a string is created, it cannot be modified.
However, it is possible to create a new string by concentrating two or more strings.



# In[6]:


### creating a string
s1 = 'this is a string, enclosed in single quotres'
s2 = "this is a string, enclosed in double quotes"
s3 = '''this is a multi-string,enclosed in triple single quotes'''
print(s1, s2, s3, sep='/n')

"""this is an informative
multi line comment,
created by using triple double quotes"""


# In[3]:


# Complier error 
a = "this cup now belongs's to INDIA" # other way to print
print(a)
a = 'this cup now belong\'s to INDIA' # \ is a escape character
a


# In[10]:


print('a/nb') # new line
print('a/tb') # tab/ four spaces
print('ab/rc') # moves the cursur to start of the line


# In[1]:


### Raw string and format-strings
# r - strings
print('c:\abc\newfolder\j.jpg')# compliers error
print('c:\\abc\\newfolder\\j.jpg')# alternative method of printing
print(r'c : \abc\newfolder\j.jpg')# using r string


# In[27]:


r, h = 5, 7
vol = (22/7)*(r**2)*h
print('the volume of a cyl, whose radius is', r,'whose h is', h, 'is', vol)
print(f'the vol of cyl whose r and h are {r} and {h} respectively is {vol}')


# In[2]:


### Format-string volume of a sphere
print(f'the vol of sphere with diameter {10} cms, volume will be {(22/7)*((10/2)**3)*(4/3)} cubic cms')


# In[25]:


## String Indexing
positive indexing
negative indexingx = 'python'
print(x[3]) # accessing h using positive indexing(left to right starts with 0 and ends with n-1)


# In[28]:


print(x[-3]) # accessing 'h'using negative indexing(right to left starts with -1 and ends index -n )


# In[30]:


x = 'abAcBde'
print(x[4])


# In[37]:


### SLICING (positive indexing)
*syntax for slicing : var[start_index,end_index,step size]
x = 'i am not sure what to take as an example'
print(len(x))
print(x[0:13])


# In[41]:


## SLICING (positive indexing)
x = 'i am not sure what to take as an example'
print(x[0:41])


# In[48]:


x = 'i am not sure what to take as an example'
print(x[0:41:1])
print(x[0:41:2])
print(x[::])
print(x[14:18])


# In[50]:


### Reversing the string
x = 'python'
print(x)
print(x[::-1])


# In[52]:


x[-1:-7:-1]
x[::-1]


# In[55]:


x = 'python'
x[6:0:-1]


# In[58]:


# To add a space between them, add " "
a, b = 'Inno', 'Minds'
c = a+b
c


# In[62]:


c *= 3
print(c)


# In[ ]:





# In[3]:


## string Concatentation ----------------adding 2 values or more
x = 'hi'
print(x+x) # x+x
print(x*5) # x+x+x+x+x+x

