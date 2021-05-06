import cv2

image = cv2.imread('C:\CV\Open_CV\Data\car.jpg')
print(image.shape) # (1500,2000,3)

resized_image = cv2.resize(image,(512,512),interpolation=cv2.INTER_AREA)
cv2.imshow('IMAGE',resized_image)

# Converting to GrayScale
gray = cv2.cvtColor(resized_image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray_Scale_Image", gray)

# Blur an Image
blur = cv2.GaussianBlur(resized_image,(5,5), cv2.BORDER_DEFAULT)
cv2.imshow('Blurred Image',blur)

# Edge Cascade
edge = cv2.Canny(resized_image,200,250)
cv2.imshow('Edge',edge)

# Blur + Edge
edge = cv2.Canny(blur,200,250)
cv2.imshow('Blurred Edge',edge)

# Dilation and Erosion
# In the Erosion, it erodes away the boundaries of foreground objects. It is used to remove small white noises from the images.
# In the Dilation, it increases the object area. The Erosion can remove the white noises, but it also shrinks our image,
# so after Erosion, if Dilation is performed, we can get better noise removal results.
# The Dilation can also be used to joins some broken parts of an object.

erosion_image = cv2.erode(resized_image,(7,7),iterations=2)
cv2.imshow('Erosion_Image', erosion_image)

dilation_image = cv2.dilate(erosion_image,(3,3),iterations=2)
cv2.imshow('Dilation_Image',dilation_image)

# Crop an Image
cropped_image = resized_image[200:350,200:350]
cv2.imshow('Cropped_Image', cropped_image)
cv2.waitKey(0)