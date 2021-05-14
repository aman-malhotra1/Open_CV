import numpy as np
import cv2

blank_image = np.zeros(shape=(512,512), dtype='uint8')
cv2.imshow("Blank_Image",blank_image)

# Draw a Rectangle and Circle
rectangle = cv2.rectangle(blank_image.copy(),pt1=(200,200), pt2=(250,300), color=(255,0,0),thickness=-1)
circle = cv2.circle(blank_image.copy(),(250,250),50,(255,0,0), -1)
cv2.imshow("Rectangle", rectangle)
cv2.imshow('Circle', circle)

# Bitwise And -> Intersecting Regions
bitwise_and = cv2.bitwise_and(src1=rectangle, src2=circle)
cv2.imshow('BitWise_And',bitwise_and)

# Bitwise Or -> Non Intersecting and Intersecting regions
bitwise_or = cv2.bitwise_or(src1=rectangle, src2=circle)
cv2.imshow("Bitwise_Or",bitwise_or)

# Bitwise XOR -> Non Intersecting regions
bitwise_xor =cv2.bitwise_xor(src1=rectangle, src2=circle)
cv2.imshow('Bitwise_XOR', bitwise_xor)

# Bitwise Not
cat_image = cv2.imread('C:\CV\Open_CV\Data\cat.jpg')
cat_image = cv2.cvtColor(cat_image,cv2.COLOR_BGR2GRAY)
ret , cat_image = cv2.threshold(cat_image,120,255,cv2.THRESH_BINARY)
cat_image_reverse = cv2.bitwise_not(cat_image)
cv2.imshow('Cat_Image',cat_image)
cv2.imshow('Cat_Image_Reverse', cat_image_reverse)
cv2.waitKey(0)


# Masking an Image
cat_image = cv2.imread('C:\CV\Open_CV\Data\cat.jpg')
cat_image = cv2.resize(cat_image,(512,512))
blank_image = np.zeros(shape=(cat_image.shape[0], cat_image.shape[1]), dtype='uint8')
rectangled_image = cv2.rectangle(blank_image.copy(),(100,100),(300,300), (255,0,0),-1)
circled_image = cv2.circle(blank_image.copy(),(blank_image.shape[0]//2,blank_image.shape[1]//2),100,255,-1)
new_image = cv2.bitwise_and(rectangled_image,circled_image)
cv2.imshow("New_Image", new_image)

masked_image = cv2.bitwise_and(cat_image,cat_image,mask=new_image)
cv2.imshow("Masked_Image",masked_image)
cv2.waitKey(0)