#!/usr/bin/env python
# coding: utf-8

# ### Assignment 4(26June)

# #### 1) Apply following operations on set : difference,is super set, is disjoint, symmetric difference update

# In[1]:


set1=({11,22,33})
set2=({33,44,22,55})
set1.difference(set2)


# In[2]:


set1=({33,55,44,11,22,33})
set2=({33,44,22,55})
set1.issuperset(set2)


# In[3]:


set1=({11,22,33})
set2=({33,44,55})
set1.isdisjoint(set2)


# In[4]:


set1=({11,22,33})
set2=({33,44,22,55})
set1.symmetric_difference_update(set2)
print(set2)


# In[9]:


''' 
   * * * *
   *     *
   *     *
   * * * *

'''
n=int(input("type input: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if(row==1 or row==4 or col==1 or col==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")


# In[12]:


'''
   *
   * * 
   * * *
   * * * *
   * * *
   * *
   *
'''
#for stating of 3 rows
n=int(input("type input: "))
for row in range(1,n+1):
    for col in range(1,row+1):
            print("*",end=" ")
    print("\n")


# for last 4 rows 

for row in range(1,n):
    for col in range(row,n):
            print("*",end=" ")
    print("\n")


# In[16]:


'''
   1
   *
   2 
   * *
   3 
   * * *
   4 
   * * * *
   5 
   * * * * *
'''
n=int(input("type input: "))
for row in range(1,n+1):
    print(row)
    for col in range(1,row+1):
        print("*",end=" ")
    print("\n")


# In[22]:


'''
   2 * * * *
   3 * * * * *....upto 9*
   4 * * * * * *....upto 16*
'''
n=int(input("type input: "))
for row in range(2,n):
    print(row,"*"*(2**row))
print("\n")


# In[ ]:




