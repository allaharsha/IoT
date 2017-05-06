from pymongo import MongoClient
import os
client = MongoClient('mongodb://harsha:harsha@ds119081.mlab.com:19081/security')
mydb = client['security']

object= mydb.intrusion.find({'user_id':'alla.sriharsha94@gmail.com'})
for obj in object:
	#print obj['user_id']
	if obj['activation']==1:
		os.system('python pir.py')
	object= mydb.intrusion.find({'user_id':'alla.sriharsha94@gmail.com'})

	
