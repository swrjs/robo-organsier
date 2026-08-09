import cv2
import os

num=11
while(num):
    vid=cv2.VideoCapture(f"./videos/{num}.MOV")
    os.makedirs(f"./frames_video_{num}", exist_ok=True)

    fps=vid.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps*0.5)
    current_frame_no = 0

    while True:
        ret, current_frame = vid.read()
        print(f"Processing frame {current_frame_no} from video {num}...")
        if not ret:
            break

        if current_frame_no % frame_interval == 0:
            print(f"Saving frame {current_frame_no} from video {num}...")
            cv2.imwrite(f"./frames_video_{num}/video_{num}_frame_{current_frame_no}.jpg", current_frame)  

        current_frame_no += 1

    vid.release()
    num -=1



