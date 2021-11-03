# TODO: color console, help in console, args

import numpy as np 

import cv2

import config as cfg
import tools 


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cfg.FACE_CASCADE_NAME)
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + cfg.EYES_CASCADE_NAME)

capture = cv2.VideoCapture(0)

frame_size = (int(capture.get(3)), int(capture.get(4)))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

while True:
	_, frame = capture.read()

	is_detected, Zframe = tools.get_detected_and_highlighted(cv2, frame)

	cv2.imshow('frame', frame)

	if cv2.waitKey(1) == ord('q'):
		break

capture.release()
cv2.destroyAllWindows()
exit()
