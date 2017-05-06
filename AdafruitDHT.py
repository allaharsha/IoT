import sys
from pymongo import MongoClient
import Adafruit_DHT
client = MongoClient('mongodb://harsha:harsha@ds119081.mlab.com:19081/security')
mydb=client['security']
import datetime
import time
# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
                '22': Adafruit_DHT.DHT22,
                '2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
    sensor = sensor_args[sys.argv[1]]
    pin = sys.argv[2]
else:
    print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#')
    print('example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4')
    sys.exit(1)
while True:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	if humidity is not None and temperature is not None:
    		x='{0:0.1f}* humidity={1:0.1f}%'.format(temperature,humidity) 
		print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
	else:
    		print('Failed to get reading. Try again!')
    		sys.exit(1)

	temperature=int(x[0]+x[1])
	myrecord = {
        	"user_id":"alla.sriharsha94@gmail.com",
        	"temp": temperature,
        	"date" : datetime.datetime.now()
        	}
	record_id = mydb.temp.insert(myrecord)	
	#time.sleep(600)
