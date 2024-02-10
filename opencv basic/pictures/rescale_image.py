import cv2
import os
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'cat.jpg')

def rescale_image(img,scale = 0.75):
    height = int(img.shape[0] * scale)
    width = int(img.shape[1] * scale)
    dimensions = (width,height)

    return cv2.resize(img,dimensions,interpolation=cv2.INTER_AREA)


img = cv2.imread(image_path)
print("Image shape",img.shape)
cv2.imshow('Original Cat',img)
resized_img = rescale_image(img,scale=0.20)
print("Resized Image shape",resized_img.shape)
cv2.imshow('Resized Cat',resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
