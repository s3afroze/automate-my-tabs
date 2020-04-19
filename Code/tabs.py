#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Fri Aug  3 09:01:08 2018

@author: Shahzeb Afroze

"""

import os 

f = 'domains.txt'

#  --- Code snippet from github - Paulo Bu
for path, dirs, files in os.walk('.'):
    if f in files:
        os.chdir(path)
        break
# ---
    
# extracting the list of domains of your site added.
domains_list = open('domains.txt','r').read()
all_domains = domains_list.strip().split('\n')

new_list = []

# Making your link viable for the browser to open.
def check_link(website_list):

    for link in website_list:
        url = link.split()

        starting = link.startswith('https://') or link.startswith('http://')
        www = link.find('www.') >= 0

        if not www and not starting:
            url.insert(0,'www.')

        if not starting:
            url.insert(0,'https://')

        '''
        initializing a variable for checking
        if the links on the file end with a domain or not. 

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

    
