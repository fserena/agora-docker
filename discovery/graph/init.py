import requests
from time import sleep

files = {'config': open('/root/graph/repo-config.ttl', 'rb')}

for i in range(5):
	try:
		rg = requests.get('http://graph:7200/rest/repositories')
		if rg.status_code == 200:
			r = requests.post('http://graph:7200/rest/repositories', files=files,
								timeout=2)
			if 300 > r.status_code >= 200:
				print 'repository created!'
				break
	except Exception as e:
		print e.message
	sleep(2)

print 'finished trying to create a repository in graphdb'

