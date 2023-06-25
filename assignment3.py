#!/usr/bin/env python
# coding: utf-8

# ### ASSIGNMENT 3(24June)

# #### 1) Take a input from the user and count character and put it into the dictionary.

# In[1]:


text=input("type text : ")
dict={}
for i in text:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


# #### 2) Take input from user check minimum one capital leter betwwen(A-Z)& small letter b/w c-z & number b/w 0-9 & special        characters { @,!,#}  [note: don't use inbuild functions ]

# In[4]:


n =input("yupe input :")
capital=0
small=0
number=0
sp1=0
sp2=0
sp3=0
for i in n:
    if(65<=ord(i)<=90):
        capital+=1
    elif(97<=ord(i)<=122):
        small+=1
    elif(48<=ord(i)<=57):
        number+=1
    elif(ord(i)==64):
        sp1+=1
    elif(ord(i)==33):
        sp2+=1
    elif(ord(i)==35):
        sp3+=1
print("capital letter found: ",capital)
print("samll letters found",small)
print("Numbers found",number)
print("@ is found",sp1)
print("! is found",sp2)
print("# is found",sp3)


# In[3]:


""" print pyramid
          *
        * * *
      * * * * * 
    * * * * * * *
    """ 


# In[5]:


n=int(input("type input: "))
for r in range(1,n+1):
    for sp in range(1,n+1-r):
        print(" ",end=" ")
    for c in range(1,(r*2)):
        print("*",end=" ")
    print("\n")


# In[ ]:




