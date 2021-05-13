import cv2

image = cv2.imread('C:\CV\Open_CV\Data\cat.jpg')
cv2.imshow('Original_Image',image)

# Averaging Blur an Image
average = cv2.blur(image,(3,3))
cv2.imshow("Average_Blurred",average)

# Averaging Blur an Image with (7*7 filter size)
average = cv2.blur(image,(7,7))
cv2.imshow("Average_Blurred_1",average)


# Gaussian Blurred
gaussian = cv2.GaussianBlur(image,(5,5),0)  # Giving Weightage to each pixle and then multiplying each pixle with weightage value and then  multiply it
cv2.imshow("Gaussian", gaussian)

# Median Blurred
median = cv2.medianBlur(image,5)
cv2.imshow("Median", median)

# A bilateral filter is non-linear, edge-preserving and noise-reducing smoothing filter. The intensity value at each pixel in an image is
# replaced by a weighted average of intensity values from nearby pixels. This weight can be based on a Gaussian distribution.
# Crucially, the weights depend not only on Euclidean distance of pixels, but also on the radiometric differences.

bilateral_filter = cv2.bilateralFilter(image,15,30,30)
cv2.imshow('Bilateral_Filter',bilateral_filter)

cv2.waitKey(0)
