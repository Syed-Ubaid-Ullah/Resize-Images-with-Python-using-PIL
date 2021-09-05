#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

size=(200,200,3)
# photos=np.ones(200,200,3)
rootDirectory = 'Image_folder'

for directoryName, subDirectoryList, fileList in os.walk(rootDirectory):
    print('Found directory: %s' % directoryName)
    for fileName in fileList:
        print('##################################################################################')
        print('>>>>>>>>>>>>>>>\t%s' % fileName)
        imageFromDirectory=Image.open(f"{rootDirectory}/{fileName}")
        print('------------------------------------')
        print('               Before')
        print('------------------------------------')
        
        imageBeforeResize=Image.open(f"{rootDirectory}/{fileName}")
        print(imageBeforeResize)
        print(f"Image Size   :{imageBeforeResize.size}")
        print(f"Image Format :{imageBeforeResize.format}")
        print(f"Image Mode   :{imageBeforeResize.mode}")


        plt.imshow(imageBeforeResize)
        plt.show()
        
        
        imageFromDirectory.thumbnail(size)
        imageInArray=np.array(imageFromDirectory)
#         print(arr)
        imageAfterResize=Image.fromarray(imageInArray)
#         img.thumbnail(size)
#         arr2=np.array(img)
#         print(arr2)
        print('------------------------------------')
        print('                After')
        print('------------------------------------')
        print(imageAfterResize)
        print(f"Image Size   :{imageAfterResize.size}")
        print(f"Image Format :{imageAfterResize.format}")
        print(f"Image Mode   :{imageAfterResize.mode}")

        plt.imshow(imageAfterResize)
        plt.show()
        print('##################################################################################')


# In[ ]:




