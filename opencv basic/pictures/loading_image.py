# Importing the Necessary Libraries like opencv and os
import cv2 as cv
import os

# Get the absolute path of the file
absolute_path = os.path.abspath(os.path.dirname(__file__))
print("Absolute path:", absolute_path)

# Join the absolute path with the image filename to get the full image path
image_path = os.path.join(absolute_path, 'cat.jpg')
print("Image path", image_path)

# Read the image using OpenCV's imread() function
img = cv.imread(image_path)

# Print the shape of the image (height, width, number of channels)
print('Image shape', img.shape)

# Print the data type of the image
print('Image data type', img.dtype)

# Print the type of the image variable
print('Image type', type(img))

# Display the image in a window titled 'Cat' using OpenCV's imshow() function
cv.imshow('Cat', img)

# Wait indefinitely for a key press. Press any key to close the window.
cv.waitKey(0)
cv.destoryAllWindows()
