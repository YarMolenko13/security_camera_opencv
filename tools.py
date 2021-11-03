import config as cfg

def get_cascades(cv2):
	f = cv2.CascadeClassifier(cv2.data.haarcascades + cfg.FACE_CASCADE_NAME)
	e = cv2.CascadeClassifier(cv2.data.haarcascades + cfg.EYES_CASCADE_NAME)
	return (f, e)

def highlight_face(cv2, frame, x, y, h, w):
	center = (x + w // 2, y + h // 2)
	if cfg.FACE_IS_ELIPSE:
		frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, cfg.FACE_HIGHLIGHT_COLOR, cfg.FACE_LINE_THICKNESS)
	else:
		frame = cv2.rectangle(frame, (x, y), (x + w, y + h), cfg.FACE_HIGHLIGHT_COLOR, cv2.LINE_4, cfg.FACE_LINE_THICKNESS)
	return (center, frame)

def highlight_eyes(cv2, frame, faceXY, x, y, h, w):
	center = (faceXY[0] + x + w//2, faceXY[1] + y + h//2)
	radius = int(round((w + h)*0.25))
	frame = cv2.circle(frame, center, radius, cfg.EYES_HIGHLIGHT_COLOR, cv2.LINE_4, cfg.EYES_LINE_THICKNESS)
	return (center, frame)

def get_detected_and_highlighted(cv2, frame):
	face_cascade, eyes_cascade = get_cascades(cv2)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray)
	is_detected = True if len(faces) > 0 else False
	
	for (x, y, h, w) in faces:
		center, frame = highlight_face(cv2, frame, x, y, h, w)
		face = frame[y:y + h, x: x + w]
		eyes = eyes_cascade.detectMultiScale(face)
		if cfg.EYES_HIGHLIGHT:
			for (x_, y_, h_, w_) in eyes:
				_, frame = highlight_eyes(cv2, frame, (x, y), x_, y_, h_, w_)

	return (is_detected, frame)

