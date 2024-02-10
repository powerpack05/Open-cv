import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

park_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'park.jpg')
print("Park path",park_path)
# Read
park = cv2.imread(park_path)
cv2.imshow('Park',park)

# Converting into Gray Scale Image
gray = cv2.cvtColor(park,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

# Blur
blur = cv2.GaussianBlur(park,ksize=(3,3),sigmaX=0,sigmaY=0,borderType=cv2.BORDER_CONSTANT)
cv2.imshow('Blue',blur)

# Edge Cascade
canny = cv2.Canny(park,122,145)
cv2.imshow('Edge Cascade',canny)

# Edge Cascade
canny = cv2.Canny(blur,122,145)
cv2.imshow('Edge Cascade on blur',canny)

# Dilating the Image
dilated = cv2.dilate(canny,(7,7),iterations=3)
cv2.imshow('Dilated Blur canny image',dilated)

# Eroded the Image
eroded = cv2.erode(dilated,(7,7),iterations=3)
cv2.imshow('Eroded',eroded)

# Resize
resize = cv2.resize(park,(500,500),interpolation=cv2.INTER_AREA)
cv2.imshow('Resized park',resize)

# Cropping
cropping = park[100:200,300:400]
cv2.imshow('cropping',cropping)

cv2.waitKey(0)
cv2.destroyAllWindows()