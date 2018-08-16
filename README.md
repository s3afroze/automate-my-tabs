# Automate my tabs

A solution for opening websites __automatically__ at date/time specified by you :relieved:.

## Why should you download?
1. Opening __emails__ at specified times so that you can remain focused on your deliverables. 
2. Opening reddit and your favourite subreddits on __happy hours__.
3. Have you bookmarked news so that it is *easier* to open them __every morning__:anguished: . Well, let's take it a step further and make that even easier.

## Prerequisites
__pip__ install _pyperclip_

## Installing
You can put the files anywhere if you know how to use the directory from the shell/terminal.
You can follow the steps below if you dont know how to use the directory:
1. Download the files in the Downloads folder.
2. In order to interact with the script, enter the following in the shell: cd Desktop/downloads/automate-my-tabs
3. Check out the README.txt file.

## How to set the time?
There are multiple ways to set the time to run the script for opening websites.

> Cronjob for __linux or Unix-like/Mac OS__ computer operating systems.
> This will give you more flexibility on specifying time. 
> Check out __cronjob.txt__ for guidance concerning specifying time. 
> I would recommend to check out this [video](https://www.youtube.com/watch?v=QZJ1drMQz1A) for more on cronjob.

> Alternatively; Another solution is by using the datetime and scheudule module in python which will support all OS. 
> Check out __schedule.txt__ for guidance concerning specifying time.

## Notes
This was done, as I was personally frusrated to regularly open tabs to catch up with news. Also, this was a good coding exercise...

## Upcoming updates
1. Using multiple text files containing list of websites.
2. Specifying time for each list of websites.
3. Chrome Extension

## Built With
Python 2.7

Libraries used:
1. __webbrowser__ - to open websites on your browser.
2. __pyperclip__ - to extract content from your clipboard.
3. __sys__ - to extract content from command-prompt/terminal.

## Acknowledgments
The resouces that has been the bedrock of my project:

1. [Automate the Boring Stuff with Python written by Al Sweigart.](https://automatetheboringstuff.com/)
2. MIT OpenCourseWare - [MIT course 6.0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) taught by Dr. Ana Bell, Prof. Eric Grimson & Prof. John Guttag.
3. Stackoverflow
4. Reddit

## License
Licensed under GNU General Public License v3.0. - afl-3.0
