import cv2
import numpy as np

# Blank Image
blank_image = np.zeros(shape=(500,500,3), dtype='uint8')
cv2.imshow("Blank_Image",blank_image)
cv2.waitKey(0)

# Draw Rectangle
cv2.rectangle(blank_image,(0,0), (blank_image.shape[0]//2,blank_image.shape[1]//2),(255,0,0),-1)
cv2.imshow("Rectangle_Image",blank_image)
cv2.waitKey(0)

# Draw Circle
cv2.circle(blank_image,(blank_image.shape[0]//2,blank_image.shape[1]//2),20,(0,255,0),-1,)
cv2.imshow('Circled_Image',blank_image)
cv2.waitKey(0)

# Draw Line
cv2.line(blank_image,(0,0),(blank_image.shape[0]//2, blank_image.shape[1]//2),(150,150,150),2)
cv2.imshow('Line_Image',blank_image)
cv2.waitKey(0)

# Write Text
cv2.putText(blank_image,'Hello There',(0,250),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
cv2.imshow('Text Image',blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()