import numpy as np
import cv2
import time
import os
import random
import sys

def videoRecorder(name):
    fps = 7.8
    width = 864
    height = 640
    video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")
    #name = "../videoFile/May/30/2"
    print("ALl logs saved in dir:", name)
    cap = cv2.VideoCapture('rtsp://user:password@IP/ch0_0.h264')
    ret = cap.set(3, 864)
    ret = cap.set(4, 480)
    cur_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    start = time.time()
    video_file_count = 1
    video_file = os.path.join(name, str(video_file_count) + ".avi")
    print("Capture video saved location : {}".format(video_file))
    # Create a video write before entering the loop
    video_writer = cv2.VideoWriter(
        video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
    )
    while cap.isOpened():
        start_time = time.time()
        ret, frame = cap.read()
        if ret == True:
            resized_frame = cv2.resize(frame, (1280, 720))
            cv2.imshow("frame", resized_frame)
            if time.time() - start > 300:
                start = time.time()
                video_file_count += 1
                video_file = os.path.join(name, str(video_file_count) + ".avi")
                video_writer = cv2.VideoWriter(
                    video_file, video_codec, fps, (int(cap.get(3)), int(cap.get(4)))
                )
            # Write the frame to the current video writer
            video_writer.write(frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            break
    cap.release()
    cv2.destroyAllWindows()
