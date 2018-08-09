import sys, pyperclip

website_list = 'websites.txt'

r = open(website_list,'r')
content = r.read()
websites_list = content.strip().split('\n')

f = open(website_list,'a')

print "\nThe current sites on your list:\n "
for count,website in enumerate(websites_list,1):
	print str(count) +')', website

if len(sys.argv)>1:
	raw = sys.argv[1:]

	for el in raw:
		content = el.split(',')

	print("\nThe following site/sites has been added to {}:").format(website_list)
	for site in content:	
		f.write(site +'\n')
		print site


else:
	user_input = raw_input("\nWould you like to add the content you have on your clipboard to the file?\nPress enter or return to add the content in your clipboard.")
	if user_input == "":
		print "\nThe link has been added to {}\n".format(website_list)
		f.write(pyperclip.paste()+ '\n')

	else:
		print "\nGot it. Have a great day!\n"








