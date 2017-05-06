from threading import Thread
import os
def security():
	os.system('python /home/pi/project/dbsr.py')
def smoke():
	os.system('python smoke.py')
def temperature():
	os.system('python /home/pi/project/test/Adafruit_Python_DHT/examples/AdafruitDHT.py 11 04')
def loop():
		thread_sec=Thread(target=temperature)
		thread_sec.start()
		thread_temp=Thread(target=security)
		thread_temp.start()			
def destroy():
        GPIO.cleanup()
if __name__ == '__main__':     # Program start from here
        print 'Press Ctrl+C to end the program...'
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child progra$
                destroy()


