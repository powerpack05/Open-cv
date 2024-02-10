import cv2 as cv
import os
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),'cat.jpg')
print("Image path ",image_path)
img = cv.imread(image_path)
bgr_to_rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(bgr_to_rgb)
plt.axis('off')
plt.title('Cat')
plt.show()

