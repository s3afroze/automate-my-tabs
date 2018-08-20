# Automate my tabs

Improving your daily browsing activity by opening websites __automatically__ at date/time specified by you.

## Why should you download?
1. Opening __emails__ at specified times so that you can remain focused on your deliverables. 
2. Opening reddit and your favourite subreddits on __happy hours__.
3. Have you bookmarked news so that it is *easier* to open them __every morning__. Well, let's take it a step further and make that even easier.
4. Opening __all__ website links instead of copying and pasting __one__ website link on the browser at a time.
5. Opening specific websites during your lunch break.
6. Opening your assignment website on weekends helping in avoiding procastinating.

## Prerequisites
1. Linux & unix-like system (such Mac OS)
2. Python 2.7 (_Most OS have python preinstalled._)

Look at notes for more details on how to check your version.
_Only required for an extra feature of adding websites to your favourite list(__not necessary__)_
3. __pip__ install _pyperclip_


## Installing
You can follow the steps below if you dont know how to use the directory and/or github:
1. Click __download or clone__ button above and download in _zip file_. 
2. Unzip the folder in case you are downloading in the __zip form__.

## Setup (2-3 minute max)
__linux or Unix-like/Mac OS__ come with a very handy tool known as __crontab__. You can read more on it [here](https://en.wikipedia.org/wiki/Cron).
1. Go to the __terminal__ in your device. This might look daunting but trust me, it's gonna get over soon.
2. Type(exclude the quotation marks) __"crontab -e"__ to set a cronjob.
3. Press __"i"__ to go in insert mode.
4. Copy(exclude the quotation marks) __"* * * * * python "__ 
5. Open the folder where you have downloaded this program and go to __Code__ folder.
6. Drag the file __multiplefiles.py__ to the terminal and drop. It is to be noted that there is __space__ between each __*__ and then __space__ after the __5th *__ and then __space__ again before you drop file. It might look something like this: 
> _* * * * * python /Users/Itsacruellife/Desktop/github_projects/automate-my-tabs/Code/multiplefiles.py_
7. Press __esc button__ and copy/write(exclude the quotations) __":wq"__ 
8. Congrats! You are done :smiley:

## How to use?
1. There is a demo.txt file to show how the to add links and set time. __Highly Recommended__
2. Currently, you can set the repeat to __daily,weekends or weekdays__(_updates coming soon for more flexibility_)
3. Create a .txt file.
4. First line should be the schedule(__set in 24 hours only__) for opening the sites. The formatting for setting time is: __daily/weekends/weekdays@__ time in _24 hours_ with __hours__ and __minuites__ split by __.__.Setting a schedule to open a list of websites at __1pm daily__ will look lke this: 
> __daily@13.00__ 

## Notes
This was done, as I was personally frusrated to regularly open tabs to catch up with sites that I visit regularly. Also, this was a good coding exercise...

## Upcoming updates
1. Using multiple text files containing list of websites.
2. Specifying time for each list of websites.
3. Chrome Extension
4. Compatibility with python 3x

## Built With
Python 2.7

## Acknowledgments
The resouces that has been the bedrock of my project:

1. [Automate the Boring Stuff with Python written by Al Sweigart.](https://automatetheboringstuff.com/)
2. MIT OpenCourseWare - [MIT course 6.0001](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/) taught by Dr. Ana Bell, Prof. Eric Grimson & Prof. John Guttag.

## License
Licensed under GNU General Public License v3.0. - afl-3.0
