#!/usr/bin/env python
# coding: utf-8

# ## Assignment 5 (27June)

# #### 1) How to swap a number without using 3rd variable except these methods

# In[1]:


a=int(input("Type first input: "))  #a=10
b=int(input("Type second input: "))   #b=20
print("Before swapping: ",a,b)
a=a+b  # a=20+10=30
b=a-b  # b=30-20=10  => b=10
a=a-b  # a=30-10=20  => a=20
print("After swapping :" ,a,b)


# #### 2) Write down a function that take data from a list if element of list is string data type so we have to remove the last word and if integer then multiply by 5 and  if element is list then remove the 0 index data from list.

# In[2]:


list2=[]
def newList(mylist):
    for i in mylist:
        if(type(i) is int):
            list2.append(i*5)
        elif(type(i) is str):
            modifiedlist=[i[:-1]]
            list2.append(modifiedlist)
        elif(type(i) is list):
            if len(i) >1:
                list2.append(i[1:])
        else:
            list2.append(i)
    return list2
        
list1=[10,'arpita',[20,30,'hey'],'kumawat',[1,2,3]]
newList=newList(list1)
print(newList)


# #### 3) Find LCM between two numbers

# In[3]:


def is_LCM(a,b):
    if(a>b):
        greater=a
    else:
        greater=b
    while True:
        if(greater%a==0 and greater%b==0):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Type 1st number: "))
num2=int(input("Type 2nd number: "))
lcm = is_LCM(num1,num2)
print("LCM of ",num1," and ",num2," is: ",lcm) 


# #### 4)  Find LCM between two numbers

# In[5]:


def is_HCF(a,b):
    if(a<b):
        smaller=a
    else:
        smaller=b
    while(smaller>=1):
        if(a % smaller==0 and b % smaller ==0):
            hcf=smaller
            break
        smaller-=1
    return hcf
num1=int(input("Type 1st number: "))
num2=int(input("Type 2nd number: "))
hcf = is_HCF(num1,num2)
print("HCF of ",num1," and ",num2," is: ",hcf)

