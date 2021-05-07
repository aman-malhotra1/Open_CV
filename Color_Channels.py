import cv2
import numpy as np

image = cv2.imread('C:\CV\Open_CV\Data\car.jpg')
image = cv2.resize(image,(512,512))

cv2.imshow("Original_Image", image)

# Image Split
blue, green , red = cv2.split(image)
print(image.shape) #(512,512,3)
print(blue.shape) # (512,512)
print(green.shape) # (512,512)
print(red.shape) # (512,512)

cv2.imshow('Blue', blue)
cv2.imshow('Red', red)
cv2.imshow('Green', green)

merged_image =cv2.merge([blue, green, red])
cv2.imshow("Merged_Image", merged_image)

# Creating blue, green , red image each with three channels
blank_image = np.zeros(shape=image.shape[:2], dtype='uint8')
blue = cv2.merge([blue,blank_image,blank_image])
green = cv2.merge([blank_image,green, blank_image])
red = cv2.merge([blank_image,blank_image,red])

cv2.imshow('Blue_1', blue)
cv2.imshow('Green_1', green)
cv2.imshow('Red_1', red)
cv2.waitKey(0)