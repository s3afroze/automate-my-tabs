import os
import webbrowser 
import schedule
import time

path = os.getcwd()
rere = os.path.join(path,'website_lists')
folder = os.listdir(rere)

list_of_files = [files for files in folder if files.endswith('.txt')]
path_to_files = [os.path.join(path,'file_path') for files in list_of_files]

def job():
	webbrowser.open_new('https://www.google.com')

schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)