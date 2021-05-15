import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C:\CV\Open_CV\Data\car.jpg',0)
image = cv2.resize(image,(512,512))
cv2.imshow('Gray_Scale_Image', image)
cv2.waitKey(0)
# create Histogram using openCV
hist = cv2.calcHist(images = [image],channels=[0],mask=None , histSize=[256],ranges=[0,256])
plt.plot(hist)
plt.show()

# Create Histogram Using Numpy
hist, bins = np.histogram(image.ravel(), bins=256,range=[0,255])
plt.plot(hist)
plt.show()


# Draw Histogram Plot for Red, Green and Blue Color
image = cv2.imread('C:/CV/Open_CV/Data/bird.jpg')
blue , red, green = cv2.split(image)

c = ['blue', 'green', 'red']
i = 0
for color in cv2.split(image):
    hist , bins = np.histogram(color,255,[0,255])
    plt.plot(hist, color = c[i])
    i += 1
plt.show()




