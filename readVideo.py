import numpy as np
import cv2

def videoR(ip_ad):
	try:
		cap = cv2.VideoCapture("rtsp://admin:cda7q14c@{0}/ch0_0.h264".format(ip_ad))
		print("Try ip: {0}".format(ip_ad))
		while(True):
		    # Capture frame-by-frame
		    ret, frame = cap.read()
		    # Our operations on the frame come here
		    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		    # Display the resulting frame
		    resized_frame = cv2.resize(frame, (820, 720))
		    cv2.imshow('ip: {0}'.format(ip_ad),resized_frame)
		    if cv2.waitKey(1) & 0xFF == ord('q'):
		    	break
		# When everything done, release the capture
		cap.release()
		cv2.destroyAllWindows()
	except:
		pass
while(True):
	videoR('192.168.1.33')
	videoR('192.168.1.34')
	videoR('192.168.1.35')
	videoR('192.168.1.36')
	videoR('192.168.1.37')
