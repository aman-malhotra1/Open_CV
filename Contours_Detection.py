# Contours are the boundries of the object . They are not same as edges
# Contours are usefull in Shape Analysis

import numpy as np
import cv2

image = cv2.imread('C:\CV\Open_CV\Data\cats.jpg')
blank_image = np.zeros(shape=image.shape, dtype='uint8')

cv2.imshow('Actual_Image',image)

# Convert into GrayScale Image
gray_scale_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray_Scale', gray_scale_image)

# Blurred Image
blurred_image = cv2.GaussianBlur(gray_scale_image,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Blurred_Image",blurred_image)

# Canny Image
canny_image = cv2.Canny(blurred_image,threshold1=70,threshold2=170)
cv2.imshow('Canny_Edges',canny_image)

# Contours
contours , heirarchies = cv2.findContours(canny_image,mode=cv2.RETR_LIST,method=cv2.CHAIN_APPROX_SIMPLE)
# RETR_EXTERNAL -> For External Lines
# RETR_LIST -> For All Lines
# RETR_TREE -> For Vertically Lines
print('Total Contours Found : ', len(contours))

cv2.drawContours(blank_image,contours,-1,(0,0,255),1) # -1 for all Lines
cv2.imshow('Contour Image', blank_image)
cv2.waitKey(0)

# Four Steps are there -> GrayScale + Blur + Canny + Contour
