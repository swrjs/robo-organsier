import cv2
import os
os.makedirs("./extracted_frames", exist_ok=True)

vid=cv2.VideoCapture("./videos/1.MOV")

fps=vid.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps*0.5)
current_frame_no = 0

while True:
    ret, current_frame = vid.read()
    print(f"Processing frame {current_frame_no}...")
    if not ret:
        break

    if current_frame_no % frame_interval == 0:
        cv2.imwrite(f"./extracted_frames/frame_{current_frame_no}.jpg", current_frame)  

    current_frame_no += 1

vid.release()



