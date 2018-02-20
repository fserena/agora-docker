import requests
from time import sleep

files = {'config': open('/root/graph/repo-config.ttl', 'rb')}

for i in range(5):
	try:
		r = requests.post('http://graph:7200/rest/repositories', files=files)
		if 300 > r.status_code >= 200:
			break
	except Exception as e:
		print e.message
	sleep(2)


