#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:01:08 2018

@author: Itsacruellife
"""

#remove spaces in website list

import webbrowser, sys, pyperclip

website_list = 'websites.txt'

domains_list = open('domains4.txt','r').read()
all_domains = domains_list.strip().split('\n')

f = open(website_list,'r')
websites = f.read()
edit = websites.strip().split('\n')
# website_list = filter(lambda x: x != '', edit)

new_list = []
n = 0
def check_link(website_list):

    for link in website_list:
        url = link.split()

        starting = link.startswith('https://') or link.startswith('http://')
        www = link.find('www.') >= 0

        if not www:
            url.insert(0,'www.')
            # www = True

        if not starting:
            url.insert(0,'https://')
            # starting = True

        for domain in all_domains:
            
            ending = link.find(domain) >= 0

            if ending:
                global n
                n = 1

        if n != 1:
            url.append('.com')

        n = 0
        new_list.append(''.join(url))
    
    return new_list

check_link(edit)

print 'Opening links....\n'
for site in new_list:
    print site
    webbrowser.open_new(site)
    
    
