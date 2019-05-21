A LinkedIn scaping tool that captures message url, conversations from message thread, and profile url. This tool uses python, selenium, chromedriver and deployed in a docker container.

This is a super simple tool with all functions in one file: run_scraper.py

##Instructions for using it in the docker container

1) Download Docker from docker.com using the 'Download desktop and take a tutorial option'

2) Create a free account and log in on the website

3) When you execute the app on your desktop, you should see the icon on your top bar
build the image that you will be using to create containers with. You need to be logged in to use docker containers on your local machine.

##Command line instructions

1) clone scraper repository

2) cd into the directory that you cloned the repository into
	'''cd/path/to/folder/you/want'''
	'''ls enter'''
	You should see the app folder Dockerfile, requirements.txt'. The app folder has a data folder which is where the scraped data will be placed in a csv file:

	'''login.viewerinfo.csv has the info from people who have viewed the linkedin page'''
	'''login.messages.csv has the info from messages linked in page'''

	It is very important that the Dockerfile and requirements.txt is one folder up from the files that are getting attached to the container. The docker container will have everything in the app folder down, not including the app folder.


3) type: 
	'''docker build -t scraper . '''
	scraper = name of the image that you will make containers from. Name this whatever you like.
	. = the current directory. Docker will look for the Dockerfile in the directory you are in so it is important you start in the right place.

4) Make a container using this image:
	'''docker run -it -w /usr/workspace -v /path/on/your/local/machine:/usr/workspace scraper bash'''

	This opens up a terminal IN the container that it has created. From here you can run the script just as you would from your local machine. 

	type in the command line prompt (ends with a #) 
	'''python run_scrape.py "username" "password"'''