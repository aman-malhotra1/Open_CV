import numpy as np
import cv2

image = cv2.imread('C:\CV\Open_CV\Data\car.jpg')
image = cv2.resize(image,(512,512))

cv2.imshow("Resized_Image",image)

# Image Translation
# -x for left , -y for up , x for right , y for down
translate_matrix = np.float32([[1,0,50],[0,1,50]])
translate_image_1 = cv2.warpAffine(image,translate_matrix,(image.shape[0],image.shape[1]))
cv2.imshow('Translate_Image_1',translate_image_1)

translate_matrix = np.float32([[1,0,-100],[0,1,-100]])
translate_image_2 = cv2.warpAffine(image,translate_matrix,(image.shape[0],image.shape[1]))
cv2.imshow('Translate_Image_2',translate_image_2)

# Rotate an Image to 45 degree angle
rotation_points = (image.shape[0]//2,image.shape[1]//2) # Rotate from center
rotation_matrix = cv2.getRotationMatrix2D(center=rotation_points,angle=45,scale=1)
rotated_image = cv2.warpAffine(src=image,M=rotation_matrix,dsize=(image.shape[0],image.shape[1]))
cv2.imshow('Rotated Image',rotated_image)

# Rotate an Image to -45 degree angle
rotation_points = (image.shape[0]//2,image.shape[1]//2) # Rotate from center
rotation_matrix = cv2.getRotationMatrix2D(center=rotation_points,angle=-45,scale=1)
rotated_image_1 = cv2.warpAffine(src=image,M=rotation_matrix,dsize=(image.shape[0],image.shape[1]))
cv2.imshow('Rotated Image_1',rotated_image_1)

# Flip an Image
flipped_image = cv2.flip(image,-1)
cv2.imshow('Flipped_Image',flipped_image)

cv2.waitKey(0)