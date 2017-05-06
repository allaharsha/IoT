from threading import Thread
import os
from gpiozero import Buzzer
import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11, GPIO.IN)
def buzzer():
	os.system('python /home/pi/project/buz.py')
def mail():
	os.system('python /home/pi/project/mail.py')
	
def telecast():
        os.system('raspivid -o - -t 0 -vf -hf -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/f0gc-d3xd-ah6z-4xwq')
def destroy():
	GPIO.cleanup()
def loop():
	while True:
       		i=GPIO.input(11)
       		if i==0:             
            		time.sleep(1)
       		elif i==1:           
             		print "Intruder detected"
	     		thread1=Thread(target=buzzer)
	     		thread1.start()
			os.system('python /home/pi/project/camera.py')
	     		#thread3=Thread(target=telecast)
			#thread3.start()
			#thread2=Thread(target=mail)
	     		#thread2.start()
			os.system('python /home/pi/project/mail.py')
             		os.system('raspivid -o - -t 0 -vf -hf -fps 30 -b 6000000 | ffmpeg -re -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -f h264 -i - -vcodec copy -acodec aac -ab 128k -g 50 -strict experimental -f flv rtmp://a.rtmp.youtube.com/live2/f0gc-d3xd-ah6z-4xwq')
			time.sleep(1)
			
if __name__ == '__main__':     # Program start from here
        print 'Press Ctrl+C to end the program...'
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child progra$
                destroy()

