from tracker.centroidtracker import CentroidTracker
from tracker.trackableobject import TrackableObject
from subprocess import call
from imutils.video import VideoStream
from imutils.video import FPS
from inquirer.themes import GreenPassion
import requests
import json
import urllib.request
import numpy as np
import inquirer
import argparse
import imutils
import logging
import time
import dlib
import cv2
#############################
call('clear', shell=True)
api_key = "398d3cf8204c51ab0e47c22d1e725174"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
print("[INFO] Checking internet Connection to get weather data")
def connect(host='https://www.google.com/'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
if connect() == True:
		print ("Connection available")
		city_name = input("Enter city name : ") 
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
		response = requests.get(complete_url) 
		x = response.json()
else:
		print ("Connection not available")
selection = [inquirer.List('detection',message = "What object you want to detect?",choices=["car","bus","bicycle","motorbike","person","boat","cat","dog","cow","sheep","bird","botle"],)]

print("[INFO] Press Enter to Sellect")

answers = inquirer.prompt(selection,theme=GreenPassion())

objex = ''.join(answers['detection'])

a = objex.split(",")

ab = "total "+a[0]

print("[INFO] Prototxt file(by default its set to (mobilenet_ssd/MobileNetSSD_deploy.prototxt)")
print("[INFO] Caffe pre-trained model file(by default its set to (mobilenet_ssd/MobileNetSSD_deploy.caffemodel)")
print("[INFO] Select Video Input(if you not selected any video file it will start webcam stream)")
print("[INFO] Press q to End Session")

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--prototxt", type=str, default="mobilenet_ssd/MobileNetSSD_deploy.prototxt",
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", type=str, default="mobilenet_ssd/MobileNetSSD_deploy.caffemodel",
	help="path to Caffe pre-trained model")
ap.add_argument("-i", "--input", type=str,
	help="path to optional input video file")
ap.add_argument("-o", "--output", type=str,
	help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.1,
	help="minimum probability to filter weak detections")
ap.add_argument("-s", "--skip-frames", type=int, default=2,
	help="# of skip frames between detections")
args = vars(ap.parse_args())
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]

print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe(args["prototxt"], args["model"])

if not args.get("input", False):
	print("[INFO] starting video stream...")
	vs = VideoStream(src=0).start()
	time.sleep(2.0)

else:
	print("[INFO] opening video file...")
	vs = cv2.VideoCapture(args["input"])

writer = None

W = None
H = None


ct = CentroidTracker(maxDisappeared=10, maxDistance=30)
trackers = []
trackableObjects = {}


totalFrames = 0
totalDown = 0
totalUp = 0

fps = FPS().start()

while True:
	frame = vs.read()
	frame = frame[1] if args.get("input", False) else frame

	if args["input"] is not None and frame is None:
		break

	frame = imutils.resize(frame, width=500)
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

	if W is None or H is None:
		(H, W) = frame.shape[:2]

	if args["output"] is not None and writer is None:
		fourcc = cv2.VideoWriter_fourcc(*"MJPG")
		writer = cv2.VideoWriter(args["output"], fourcc, 30,
			(W, H), True)

	status = "Waiting"
	cv2.line(frame, (0, H // 2), (W, H // 2), (10, 250, 22), 5)
	rects = []

	if totalFrames % args["skip_frames"] == 0:
		status = "Detecting"
		cv2.line(frame, (0, H // 2), (W, H // 2), (219, 194, 50), 5)

		trackers = []

		blob = cv2.dnn.blobFromImage(frame, 0.007843, (W, H), 80)
		net.setInput(blob)
		detections = net.forward()

		for i in np.arange(0, detections.shape[2]):
			confidence = detections[0, 0, i, 2]

			if confidence > args["confidence"]:

				itemId = int(detections[0, 0, i, 1])

				if CLASSES[itemId] != a[0]:
					continue

				box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
				(startX, startY, endX, endY) = box.astype("int")

				tracker = dlib.correlation_tracker()
				rect = dlib.rectangle(startX, startY, endX, endY)
				tracker.start_track(rgb, rect)

				trackers.append(tracker)

	else:
		for tracker in trackers:
			status = "Tracking"
			cv2.line(frame, (0, H // 2), (W, H // 2), (255, 10, 10), 5)

			tracker.update(rgb)
			pos = tracker.get_position()

			startX = int(pos.left())
			startY = int(pos.top())
			endX = int(pos.right())
			endY = int(pos.bottom())

			rects.append((startX, startY, endX, endY))

	objects = ct.update(rects)

	
	for (objectID, centroid) in objects.items():
		
		to = trackableObjects.get(objectID, None)

		if to is None:
			to = TrackableObject(objectID, centroid)

		else:
			y = [c[1] for c in to.centroids]
			direction = centroid[1] - np.mean(y)
			to.centroids.append(centroid)

			if not to.counted:
				if direction < 0 and centroid[1] < H // 2:
					totalUp += 1
					print (("1 {} has passed UP at {}").format(a[0],time.strftime("%D:%H:%M:%S")))
					to.counted = True


				elif direction > 0 and centroid[1] > H // 2:
					totalDown += 1
					print (("1 {} has passed down at {}").format(a[0],time.strftime("%D:%H:%M:%S")))
					to.counted = True

		trackableObjects[objectID] = to

		
		text = "ID {}".format(objectID)
		cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
		cv2.circle(frame, (centroid[0], centroid[1]), 4, (0,255,0), -1)

	info = [
		("Passed ",a[0],totalDown),
	]

	for (i, (k, v,b)) in enumerate(info):
		text = "{}{}: {}".format(k , v, b)
		cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
			cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 255), 2,cv2.LINE_AA)

	if writer is not None:
		writer.write(frame)

	
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("q"):
		break
        totalFrames += 1
	fps.update()

fps.stop()
print ("####################################################################")
if x["cod"] != "404": 
  
    y = x["main"] 
  
    current_temperature = y["temp"] 
  
    current_temp_min = y["temp_min"] 
  
    current_temp_max = y["temp_max"]
  
    current_humidiy = y["humidity"] 
  
    z = x["weather"] 
  
    weather_description = z[0]["description"] 
  
    v = x["wind"] 
  
    wind_speed = v["speed"] 
    wind_direct = v["deg"]
  
    q = x["clouds"] 
  
    cloudiness = q["all"] 


    print(" Temperature (in kelvin unit) = " +
                    str(current_temperature) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n Wind speed (in m/s) = " +
                    str(wind_speed) +
          "\n cloudiness (in %) = " +
                    str(cloudiness) +
          "\n description = " +
                    str(weather_description)) 

else: 
    print(" City Not Found ") 

print ("####################################################################")
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] Selected Objects = "+ str(objex))
print("[INFO] Total {} Passed Down {}".format(a[0],totalDown))
print("[INFO] Total {} Passed Up {}".format(a[0],totalUp))
tdown = str(totalDown)
tup = str(totalUp)
ntime = str(time.strftime("%D:%H:%M:%S"))
logging.basicConfig(filename='data.csv', level=logging.DEBUG,format='%(message)s')
logging.debug('%s,%s,%s,%s,%s,%s,%s,%s',ntime,tdown,tup,current_temperature,current_humidiy,wind_speed,cloudiness,weather_description)

if writer is not None:
	writer.release()

if not args.get("input", False):
	vs.stop()

else:
	vs.release()

# close any open windows
cv2.destroyAllWindows()
