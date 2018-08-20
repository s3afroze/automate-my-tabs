#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

Created on Fri Aug  3 09:01:08 2018
@author: Shahzeb Afroze
Linkedin: https://www.linkedin.com/in/shahzebafroze/

An algorithim to add your favourite sites to the list. 

"""

import sys
import pyperclip

# extracting the websitelist to show the user.
file = 'websites.txt'
with open(file,'r') as r:
	
	# read the time and it won't be part of the UI
	time = r.readline()
	content = r.read()
	websites_list = content.strip().split('\n')
	del_empty_strings = [website for website in websites_list if website != ""]

# UI 
print "\n->The current list of websites:\n "

for count,website in enumerate(del_empty_strings,1):
	print str(count) +')', website

def update_list(final_list):

	print("\n->The updated website list in {}:\n").format(file)
	
	f = open(file,'w')
	n = len(final_list[count-1])

	if n>40:
		n=30

	for i,site in enumerate(final_list,1):

		if i == count+1:
			print "updates".center(n+4,'-')
			print ""

		print str(i) + ") " + site
		f.write(site + '\n\n')

	f.close()
	print ""
	


# Does the user want to add from clipboard or directly?

if len(sys.argv)>1:

	# command line content held by the variable - returned in list data type
	raw = sys.argv[1:]

	# convert the "string" with args to split elements 
	for el in raw:
		content = el.split(',')

	final_list = del_empty_strings + content 
	update_list(final_list)
	

else:

	clipboard = str(pyperclip.paste().strip())

	print "\n->Would you like to add the following link to the file?\n"
	print str(count + 1) + ") " + clipboard

	user_input = raw_input("\n->Press enter or return to add the content in your clipboard.")

	if user_input == "" :
		final_list = del_empty_strings[:]
		final_list.append(clipboard)
		update_list(final_list)








