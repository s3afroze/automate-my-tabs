#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""

Created on Fri Aug  3 09:01:08 2018
@author: Shahzeb Afroze
Linkedin: https://www.linkedin.com/in/shahzebafroze/

An algorithim to open your favourite sites on specific times. 

"""

import webbrowser

website_list = 'websites.txt'

# extracting the list of domains of your site added.
domains_list = open('domains4.txt','r').read()
all_domains = domains_list.strip().split('\n')

# extracting the list of websites from the file.
f = open(website_list,'r')
edit = f.read()
websites = edit.strip().split('\n')


new_list = []
n = 0

# Making your link viable for the browser to open.
def check_link(website_list):

    for link in website_list:
        url = link.split()

        starting = link.startswith('https://') or link.startswith('http://')
        www = link.find('www.') >= 0

        if not www:
            url.insert(0,'www.')

        if not starting:
            url.insert(0,'https://')

'''
initializing a variable for checking
if the domain ends properly. 
'''
        found = False
        for domain in all_domains:
            
            ending = link.find(domain) >= 0

            if ending:
                found = True

        if not found:
            url.append('.com')

        new_list.append(''.join(url))
    
    return new_list

check_link(websites)

print 'Opening links....\n'

for site in new_list:
    print site
    webbrowser.open_new(site)
    
    
