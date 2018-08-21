#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

@author: Shahzeb Afroze
Linkedin: https://www.linkedin.com/in/shahzebafroze/

An algorithim to open your favourite sites automatically. 

"""

import os
import webbrowser
from datetime import datetime,time,timedelta
import tabs

f = 'domains.txt'

# Code snippet from github - Paulo Bu
for path, dirs, files in os.walk('.'):
    if f in files:
        os.chdir(path)
        break
    
# extracting the list of domains of your site added.
domains_list = open('domains.txt','r').read()
all_domains = domains_list.strip().split('\n')

#changed directory to main_folder
os.chdir('..')

#changed directory to website lists
os.chdir('website_lists')
folder = os.listdir(os.getcwd())

path_to_files = [files for files in folder if files.endswith('.txt')]

d = {}
# fill the dict 
d['weekdays'] = ['Monday','Tuesday','Wednesday','Thursday','Friday']
d['weekends'] = ['Saturday','Sunday']
d['daily'] = d['weekdays'] + d['weekends']

for file in path_to_files:

	with open(file,'r') as f:

		datetimestr = f.readline().strip()
		edit = f.read()
		websites = edit.strip().split('\n')
		del_empty_str = [ws for ws in websites if ws != ""]

	# Daily 1.30PM(User requirement) - We will tackle with the first part later
	schedule = datetimestr.split('@')
	timestr = schedule[1]
	repeat = schedule[0].lower()
	
	#coversion
	timeobj = datetime.strptime(timestr,'%H.%M').time()
	

	today = datetime.now()
	day_today = today.strftime("%A")
	timerightnow = today.time()
	hour_and_min = time(timerightnow.hour,timerightnow.minute)

	# Control flow for the days to be scheduled

	condition = (hour_and_min == timeobj)
	
	if condition:
		for el in d.keys():
			if el == repeat:
				if day_today in d[el]:
					new_list = tabs.check_link(del_empty_str)
					
					for site in new_list:
							webbrowser.open_new(site)
		
			
				




# specific days which will be appended
