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


# extracted content from your clipboard
clipboard = pyperclip.paste().strip()


# extracting the websitelist to show the user.
website_list = 'websites.txt'
r = open(website_list,'r')
content = r.read()
websites_list = content.strip().split('\n')

# opening file to make additions
f = open(website_list,'a')

# UI 
print "\n->The current list of websites:\n "
for count,website in enumerate(websites_list,1):
	print str(count) +')', website


# Does the user want to add from clipboard or directly?

if len(sys.argv)>1:

	# command line content held by the variable - raw
	raw = sys.argv[1:]

	for el in raw:
		content = el.split(',')

	print("->The following link/links has been added to {}:\n").format(website_list)
	
	for i,site in enumerate(content,count+1):
		
		f.write(site +'\n')
		print str(i) + ") " + site

	print ""


else:

	print "\n->Would you like to add the following link to the file?\n"
	print str(count + 1) + ") " + clipboard

	user_input = raw_input("\n->Press enter or return to add the content in your clipboard.")

	if user_input == "":
		print "->The link has been successfully added to {}\n".format(website_list)
		f.write(clipboard + '\n')








