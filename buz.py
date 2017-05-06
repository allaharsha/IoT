import RPi.GPIO as GPIO
import time

beep=12
def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(beep,GPIO.OUT)
	GPIO.output(beep,GPIO.HIGH)
def loop():
	count=0
	#while count<1000:
	while True:
		GPIO.output(beep,GPIO.LOW)
        	time.sleep(0.001)
        	GPIO.output(beep,GPIO.HIGH)
        	time.sleep(0.001)
		count+=1
def destroy():
        GPIO.output(beep, GPIO.HIGH)    # beep off
        GPIO.cleanup() 
if __name__ == '__main__':     # Program start from here
        print 'Press Ctrl+C to end the program...'
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child progra$
                destroy()

