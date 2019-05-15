from copy import deepcopy
from collections import namedtuple
from queue import Queue
import time
import mysql.connector
from flask import Flask
import json
import random, string
import threading

app = Flask(__name__)

diseases= {}
db_lock = threading.Lock()

def print_diseases( de_printat):
	data = []
	config = {
		'user': 'root',
		'password': 'root',
		'host': 'db',
		'port': '3306',
		'database': 'heart_diseases_db'
	}
	connection = mysql.connector.connect(**config)
	cursor = connection.cursor()
	cursor.execute('SELECT * from heart_diseases')

	

	for x in cursor:
		data.append(x)

	cursor.close()
	connection.close()
	print(data)

	return(data)



@app.route('/search/<de_printat>', methods=['GET'])
def search(de_printat):
	data = print_diseases(de_printat)
	#for () in data:
	(ID, name1, provenance, critical_level, recomandation, recovery_days) = data[0] 
	return json.dumps({'ID': ID,'name1': name1,'provenance': provenance, 
	'critical_level': critical_level, 'recomandation':recomandation, 'recovery_days':recovery_days})

	#return json.dumps({'ID': data[0],'name1': data[1],'provenance': data[2], 
	#'critical_level': data[3], 'recomandation':data[4], 'recovery_days':data[5]})


if __name__ == '__main__':
	app.run(host='0.0.0.0')