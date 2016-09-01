import subprocess
import re
import os

ps = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE).communicate()[0]
processes = ps.split('\n')

sep = re.compile('[\s]+')
for row in processes:
	if 'app.py' in sep.split(row)[-1]:
		os.system('sudo kill -9 ' + sep.split(row)[1])
