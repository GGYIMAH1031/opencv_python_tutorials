# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 13:08:09 2015

@author: Johnny
"""

#%%
import cv2
import numpy as np

#%%
img = cv2.imread('star2.jpg', 0)

#%%
ret, thresh = cv2.threshold(img, 127, 255, 0)
#%%
#image, contours, hierarchy = cv2.findContours(thresh, 1, 2)
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)
#%%
cv2.imshow("img", img)
cv2.imshow("thresh", thresh)
cv2.imshow("image", image)
cv2.waitKey()
cv2.destroyAllWindows()

#%%
cnt = contours[0]
area = cv2.contourArea(cnt)
print area