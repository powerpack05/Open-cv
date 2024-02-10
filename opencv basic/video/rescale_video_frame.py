import cv2
import os

video_path = "dog.mp4"  # Assuming the video is in the same directory as the script

def rescaled_video_frame(frame, scale=0.75):
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

capture = cv2.VideoCapture(video_path)
while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break

    cv2.imshow('Original Frame', frame)
    resized_frame = rescaled_video_frame(frame, scale=0.20)
    cv2.imshow('Resized Frame', resized_frame)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
