import os
import webbrowser
from datetime import datetime,date,time
import time
import tabs

path = os.getcwd()
rere = os.path.join(path,'website_lists')
folder = os.listdir(rere)

list_of_files = [files for files in folder if files.endswith('.txt')]
path_to_files = [os.path.join(path,files) for files in list_of_files]

today = datetime.now()

# extracting the list of domains of your site added.
domains_list = open('domains.txt','r').read()
all_domains = domains_list.strip().split('\n')

d = {}
# fill the dict 
d['weekdays'] = ['Monday','Tuesday','Wednesday','Thursday','Friday']
d['weekends'] = ['Saturday','Sunday']
d['daily'] = weekdays + weekends

for file in path_to_files:

	new_list = []
	
	with open(file,'r') as f:

		datetimestr = f.readline().strip()
		edit = f.read()
	    websites = edit.strip().split('\n')

	# Daily 1.30PM(User requirement) - We will tackle with the first part later
	schedule = datetimestr.split()
	timestr = schedule[1]
	timels = timestr.split('.')
	repeat = schedule[0].lower()

	# Have to convert string to int
	hour,minuite = [int(el) for el in timels]
	timeobj = time(hour,minuite)

	# Later implemention of specific dates and range 
	# # The obj will be used to update the date everyday
	# dateobj  = today.date()

	# # The new obj will be a combination of the two
	# datetime = datetime.combine(dateobj,timeobj)

	day_today = today.strftime("%A")

	# Control flow for the days to be scheduled

	for el in d.keys():
		if el == repeat:
			if day_today in d[el]:
				tabs.check_link(websites)
				




# specific days which will be appended
