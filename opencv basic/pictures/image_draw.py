import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'cat.jpg')
print("Image path",image_path)

blank_image = np.zeros((500,500,3),dtype='uint8')
print(type(blank_image))
print(blank_image.dtype)

# 1.paint the image in certain colour
# as open cv gets the color in Blue,Green,Red
# blank_image[:] = 255,0,0
# cv2.imshow('Blank',blank_image)

# 2. Draw a Rectangle
# cv2.rectangle(blank_image,(0,0),(250,250),(0,255,0),thickness=10)
# cv2.imshow('Rectangle',blank_image)
#
# cv2.rectangle(blank_image,(0,0),(blank_image.shape[1]//2,blank_image.shape[0]//2),(0,0,255),thickness=1)
# cv2.imshow('Rectangle',blank_image)
#
# cv2.rectangle(blank_image,(0,0),(250,500),(255,0,0),thickness=cv2.FILLED)
# cv2.imshow('Rectangle',blank_image)
#
cv2.rectangle(blank_image,(0,0),(250,500),(123,222,225),thickness=-1)
cv2.imshow('Rectangle',blank_image)

# 3. Draw a circle
cv2.circle(blank_image,(blank_image.shape[1]//2,blank_image.shape[0]//2),40,(0,255,0),thickness=10)
cv2.imshow('Circle',blank_image)
# 4.Draw a line
cv2.line(blank_image, (0, 0), (250, 0), color=(111, 222, 123), thickness=10)
cv2.imshow('Line1', blank_image)
cv2.line(blank_image, (0, 0), (0, 250), color=(100, 200, 255), thickness=10)
cv2.imshow('Line2', blank_image)
cv2.line(blank_image, (0, 250), (250, 250), color=(0, 255, 0), thickness=10)
cv2.imshow('Line3', blank_image)
cv2.line(blank_image,pt1=(250,0),pt2=(250,250),color=(255,0,0),thickness=10)
cv2.imshow('Line4',blank_image)

# 5.Write a Text
cv2.putText(blank_image,'Farheen Syed',(123,255),cv2.FONT_HERSHEY_PLAIN,1.0,color=(123,255,255))
cv2.imshow('Text',blank_image)
cv2.waitKey(0)






# paint the image in certain color
# img = cv2.imread(image_path)
# print(img.max(),img.min())
# cv2.imshow('Cat',img)
cv2.waitKey(0)
cv2.destroyAllWindows()