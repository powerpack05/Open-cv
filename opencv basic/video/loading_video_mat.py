import cv2
import os
import matplotlib.pyplot as plt

absolute_path = os.path.abspath(os.path.dirname(__file__))
print(f"Absolute path {absolute_path}")
video_path = os.path.join(absolute_path,'dog.mp4')
print('Video path',video_path)

capture = cv2.VideoCapture(video_path)
frames_count = 0

while True:
    isTrue,frame = capture.read()

    if not isTrue:
        break

    frames_count+=1

    bgr_2_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    plt.imshow(bgr_2_rgb)
    plt.axis('off')
    plt.title(f'Frame - {frames_count}')
    plt.show()
    
    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

print('total frames',frames_count)
capture.release()
cv2.destroyAllWindows()
