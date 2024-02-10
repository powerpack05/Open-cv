# Importing the Necessary Libraries like opencv and os
import cv2 as cv
import os

# Getting the absolute path of the current directory
absolute_path = os.path.abspath(os.path.dirname(__file__))
print("Absolute Image path", absolute_path)

# Constructing the full path to the video file
video_path = os.path.join(absolute_path, 'dog.mp4')
print("Video path", video_path)

# Creating a VideoCapture object to read the video file
capture = cv.VideoCapture(video_path)

# Initializing a variable to count the frames
frames_count = 0

# Looping through each frame of the video
while True:
    # Reading a frame from the video
    isTrue, frame = capture.read()

    # Checking if the frame was read successfully
    if not isTrue:
        break

    # Incrementing the frame count
    frames_count += 1

    # Displaying the current frame
    cv.imshow(f'Frame - {frames_count}', frame)

    # Checking for key press 'd' to exit the loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Printing the total number of frames processed
print(f'Total frames', frames_count)

# Releasing the VideoCapture object
capture.release()

# Closing all OpenCV windows
cv.destroyAllWindows()
