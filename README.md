A LinkedIn scaping tool that captures message url, conversations from message thread, and profile url. This tool uses python, selenium, chromedriver and deployed in a docker container built on [joyzoursky/docker-python-chromedriver image](https://github.com/joyzoursky/docker-python-chromedriver)

This is a super simple tool with all functions in one file: run_scraper.py

## Instructions for using it in the docker container

1) Download Docker from docker.com using the 'Download desktop and take a tutorial option'

2) Create a free account and log in on the website

3) When you execute the app on your desktop, you should see the icon on your top bar
build the image that you will be using to create containers with. You need to be logged in to use docker containers on your local machine.

## File Structure

1) clone this scraper repository

2) cd into the directory that you cloned the repository into
	'''
	cd /path/to/folder/you/want
	'''
	'''
	ls 
	
	On your local machine, you should see the app folder, Dockerfile, and requirements.txt. 
	,,,

3) It is very important that the Dockerfile and requirements.txt is one folder up from app. Docker builds the image with the Dockerfile and requirements.txt. When you run the container, it will contain everything from the app folder down and not include the app folder itself.

## Data Information

	Scraped information is put into 2 csv's in app/data 
	
	'''
	{login_name}.viewerinfo.csv: profile url, first name, last name of people who viewed the profile
	'''
	'''
	{login_name}.messages.csv: profile url, first name, last name, full message thread, message url from messages page
	'''
 
 ## Command Line Instructions


1) Build the image on your local machine

	'''
	docker build -t scraper . 
	'''

	Note: 
	scraper = name of the image that you will make containers from. Name this whatever you like.
	. = the current directory. Docker will look for the Dockerfile in the directory you are in so it is important you start in the right place.

2) Make a container using the built image

	'''
	docker run -it -w /usr/workspace -v /path/on/your/local/machine:/usr/workspace scraper bash
	'''

	This opens up a terminal IN the container that was created. From here you can run the script just as you would from your local machine. 

3) type in the command line of the container

	'''
	python run_scrape.py "username" "password"
	'''