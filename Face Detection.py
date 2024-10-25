#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[2]:


import cv2


# In[ ]:





# In[ ]:





# In[3]:


video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10)== ord("a"):
        break
        
video_cap.release()    


# In[ ]:




