# TODO: color console, help in console, args

import numpy as np 
import datetime
import time
import cv2

import config as cfg
import tools 


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cfg.FACE_CASCADE_NAME)
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cfg.EYES_CASCADE_NAME)

capture = cv2.VideoCapture(0)

frame_size = (int(capture.get(3)), int(capture.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

stopped_time = None
is_recording = False

while True:
	_, frame = capture.read()

	is_detected, frame = tools.get_detected_and_highlighted(cv2, frame)

	if is_detected:
		if not is_recording:
			is_recording = True
			current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
			out = cv2.VideoWriter(f"output/{current_time}.mp4", fourcc, 20, frame_size)
			print('Start recording!')
		else:
			stopped_time = time.time()
			out.write(frame)
	if not is_detected and time.time() - stopped_time >= cfg.SECONDS_TO_RECORD_AFTER_DETECTION:
		if is_recording:
			is_recording = False
			out.release()
			print('Stop recording!')

	cv2.imshow('Cam', frame)

	if cv2.waitKey(1) == ord('q'):
		break

out.release()
capture.release()
cv2.destroyAllWindows()
exit()
