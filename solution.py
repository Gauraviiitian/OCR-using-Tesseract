#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import OpenCV, Tesseract, Matplotlib
import cv2
import pytesseract
import matplotlib.pyplot as plt
import sys


# In[2]:

# Configure the OCR Engine
config = ('-l eng --oem 1 --psm 3')


# In[3]:


#Read the image as Grayscale image
img = raw_input("Enter the path of the image: ")
im = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

#Binarizing the image
#(thresh, im) = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#plt.imshow(im)


# In[4]:


# Denoising images for better accuracy
#im = cv2.fastNlMeansDenoising(im, 5, 7, 21)

#upscaling the image for better performancem
dim = list(im.shape)
per = 200 #percentage of upscaling
dim[0] = (dim[0]*per)//100
dim[1] = (dim[1]*per)//100
im = cv2.resize(im, (dim[1], dim[0]), interpolation = cv2.INTER_AREA) # resizing image
plt.imshow(im)


# In[5]:


text = pytesseract.image_to_string(im, config=config) # Running the Tesseract OCR Engine


# In[6]:


text = text.split() #Split the whole output in words
print text #print the list


# In[ ]:




