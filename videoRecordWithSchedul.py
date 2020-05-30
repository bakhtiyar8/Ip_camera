import schedule
import time
import datetime
import os
from videoRecorder import videoRecorder

def run():
	# Date and Directory will be writeen as date and hour
	directory = str(datetime.datetime.today().strftime("Y-%Y-M-%m-D-%d-H-%H"))
	# Perant Directory path
	parent_dir = "../videoFile/"
	# Path
	path = os.path.join(parent_dir, directory)
	# Create the directory
	os.mkdir(path)
	print("Directory '% s' created" % directory)
  # videoRecorder function sent folder path
	videoRecorder(path)
#schedule.every(10).minutes.do(run)
#every 4 hours it will create folder and save video file in it
schedule.every(4).hours.do(run)
#add your start time
schedule.every().day.at("19:07").do(run)
#schedule.every(5).to(10).minutes.do(run)
#schedule.every().monday.do(run)

while True:
	schedule.run_pending()
	time.sleep(1)
