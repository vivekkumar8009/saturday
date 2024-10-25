#!/usr/bin/env python
# coding: utf-8

# In[1]:


import extract_msg
import re
import pandas as pd
import re
from bs4 import BeautifulSoup
import urllib.request
import requests
import pandas as pd


# In[2]:


f=(r"C:\Users\vivek.kumar131\Downloads\IPAllocation sync failure Details.msg")


# In[3]:


msg = extract_msg.Message(f)


# In[4]:


msg_sender = msg.sender
msg_date = msg.date
msg_subj = msg.subject
msg_message = msg.htmlBody

print('Sender: {}'.format(msg_sender))
print('Sent On: {}'.format(msg_date))
print('Subject: {}'.format(msg_subj))
print('Body: {}'.format(msg_message.decode()))


# In[5]:


type(msg)


# In[6]:


dir(msg)


# In[7]:


html_string = msg_message.decode('utf-8')


# In[8]:


htmlParse = BeautifulSoup(html_string, 'html.parser')


# In[9]:


for para in htmlParse.find_all("p"):
    print(para.get_text())


# In[10]:


data=html_string
report_name = re.findall('REPORT OF FAILED ALLOCATION DURING [A-Z ]*', data)[0].replace('REPORT OF FAILED ALLOCATION DURING ','')
date = re.findall('Date:[a-zA-Z0-9,: ]*', data)[0].replace("Date: ","")
CIDN = re.findall('CIDN : [0-9]*', data)[0].replace("CIDN : ","")
Total_users = re.findall('Total users failed is [0-9]*', data)[0].replace("Total users failed is ","")


# In[11]:


report_name


# In[12]:


date


# In[13]:


CIDN


# In[14]:


Total_users


# In[15]:


Network_ID = re.findall('[N][0-9]+[R]',data)
Auth_service = re.findall("wl[0-9a-z.]*.com|dl[0-9a-z.]*.au",data)
user_ID = re.findall("0015[0-9]+|ase[0-9]+",data)
reason = re.findall("The IP Address .*\n*.*\n*.*Update",data)
col =["Network_ID","Auth_service","User_ID","Reason"]


# In[16]:


data1 = pd.DataFrame(list(zip(Network_ID,Auth_service,user_ID,reason)), columns =col)


# In[17]:


data1


# In[18]:


f = open('cleaned.txt', 'wt')


# In[19]:


f = open('cleaned.txt', 'wt')
f.write(f"Report name: {report_name}\n")
f.write(f"Date: {date}\n")
f.write(f"CIDN Number: {CIDN}\n")
f.write(f"Total failed users: {Total_users}\n\n\n")
f.write(data1.to_string())
f.close()


# In[20]:


print(open('cleaned.txt').read())


# In[ ]:




