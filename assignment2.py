#!/usr/bin/env python
# coding: utf-8

# ### ASSIGNMENT 2
# #### check a string is palindrome for any string using for loop(starting and ending character is same)

# In[1]:


x=input("enter a string : ")
y=''
for i in x:
    y=i+y
if(x==y):
    print(x," is an palindrome")
else:
    print(x ," is not an palindrome")


# #### take input from user and count how many vowels are their inside it ..total count

# In[2]:


x=input("Type Input : ")
count=0
for i in x:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count+=1
print(count)


# #### take a input from user and count number of individual vowels...a=0,e=2,i=1,u=3

# In[3]:


x=input("type input : ")
j=0
k=0
l=0
m=0
n=0
for i in x:
    if(i=='a'):
        j+=1
    if(i=='e'):
        k+=1
    if(i=='i'):
        l+=1
    if(i=='o'):
        m+=1
    if(i=='u'):
        n+=1
print("a=",j," ,e=",k," ,i=",l," ,o=",m," ,u=",n)


# #### take a input from user and wherever we find vowel then replace it with #

# In[4]:


x=input("type input : ")
for i in x:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        x=x.replace(i,'#')
print(x)


# #### list in which all are int...if element is int then square of that no. and appnd in new list and if other type of data then append in new list using while loop

# In[5]:


mylist=[10,20,30,40,'arpita']
sqlist=[]
newlist=[]
len(mylist)
i=0
while(i<len(mylist)):
    if(type(mylist[i]) is int):
        sqlist.append(mylist[i]**2)
        i+=1
    else:
        newlist.append(mylist[i])
        i+=1
print(sqlist)
print(newlist)
   


# #### take a input from a user if input is string datatype then get all the unique (no duplicate words)word from that string no regular expression/ no inbuilt -->alphanumeric, unique,(x)

# In[6]:


mylist=[]
newlist=[]
x=input("Type input ")
for i in x:
    mylist.append(i)
print(mylist)
for j in x:
    for k in range(1,len(mylist)):
        if(j!=k):
            newlist.append(j)
        
    break
print(newlist)


# In[ ]:




