import requests
from time import sleep

for i in range(10):
	try:
		rg = requests.get('http://fountain:5000/prefixes', headers={'Accept': 'application/json'})
		if rg.status_code == 200:
			break
	except Exception as e:
		print e.message
	sleep(2)

