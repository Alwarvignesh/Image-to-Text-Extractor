#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Extract text from image file
get_ipython().system('pip install pytesseract pillow')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
image_path= r'C:\Users\nsure\Pictures\Nature_image.jpg'
image=Image.open(image_path)
value=pytesseract.image_to_string(image)
img=mpimg.imread(image_path)
print("\n Text with Image:-")
plt.imshow(img)
plt.show()
print("\n After Extract the text from image:-\n")
print(value)


# In[ ]:





# In[ ]:




