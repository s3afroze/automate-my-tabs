#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 09:01:08 2018

@author: Itsacruellife
"""

#remove spaces in website list

import webbrowser, sys, pyperclip

website_list = 'websites.txt'

variations_of_yes = open ('variation_of_yes.txt','r').read()
yes_list = variations_of_yes.strip().split('\n')

domains_list = open('domains.txt','r').read()
all_domains = domains_list.strip().split('\n')

f = open(website_list,'a')

if len(sys.argv) > 1:
# Get address from command line.
    raw = ' '.join(sys.argv[1:])
    f.write('\n'+ raw)
    
else:
    answer = raw_input("Would you like to add the site that you have on your clipboard to the {} file? ".format(website_list))
    
    if answer in yes_list:
        f.write('\n' + pyperclip.paste())
        print 'added'
    
    else:   
        print "Got it!"
                
f = open(website_list,'r')
websites = f.read()
edit = websites.strip().split('\n')
website_list = filter(lambda x: x != '', edit)

for el in website_list:
    print el

new_list = []

def check_link(website_list):

    for link in website_list:
        for domain in all_domains:
            
            starting = link.startswith('https://') or link.startswith('http://')
            ending = link.find(domain) >= 0
            
            if (not starting and not ending):
                approved_link = 'https://' + link + '.com'
                starting = True
                ending = True 
            
            elif not ending:
                approved_link = link + '.com'
                ending = True 
            
            elif not starting:
                approved_link = 'https://' + link
                starting = True
                break
            
            elif starting and ending:
                approved_link = link
                break              
            
        new_list.append(approved_link)
                
    return new_list

check_link(website_list)
     
for site in new_list:
    print site
    webbrowser.open_new(site)
    
    
#  