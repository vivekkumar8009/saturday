#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install ultralytics')


# In[10]:


from ultralytics import YOLO

# Create a new YOLO model from scratch
#model = YOLO('yolov8n.yaml')

# Load a pretrained YOLO model (recommended for training)
#ccc


# In[5]:


# Train the model using the 'coco128.yaml' dataset for 3 epochs
results = model.train(data='coco128.yaml', epochs=3)


# In[4]:


# Evaluate the model's performance on the validation set
results = model.val()


# In[22]:


results = model.predict("https://www.irishcentral.com/uploads/article/128594/tourists-take-selfie-in-dublin-getty.jpg", save=True)


# In[23]:


import cv2
import numpy as np
from matplotlib import pyplot as plt


# In[26]:


from PIL import Image, ImageDraw


# In[29]:


plt.imshow(results[0].orig_img)
plt.show()


# In[69]:


box =results[0].boxes.data[1]


# In[71]:


box


# In[70]:


cropped = results[0].orig_img[int(box[1]):int(box[3]),int(box[0]):int(box[2])]


# In[55]:


plt.imshow(cropped)
plt.show()


# In[65]:


for i,index in enumerate(results[0].boxes.data):
    box =results[0].boxes.data[i]
    cropped = results[0].orig_img[int(box[1]):int(box[3]),int(box[0]):int(box[2])]
    plt.imshow(cropped)
    print("Accuracy %",float(box[4]*100),results[0].names[int(box[5])])
    plt.show()
    


# In[62]:


results[0].names[0]


# In[66]:


def drawBox(frame, box):
    #x,y,w,h = int(box[0]), int(box[1]),int(box[2]),int(box[3])
    int(box[0]-x), int(box[1]-y),int(box[2]-w),int(box[3]-h)
    base_image_h,base_image_w,_= final_dimension
    print(base_image_w,base_image_h)
    print(base_image_w,w-x,base_image_w,x+w)


# In[68]:


frame


# In[ ]:




