A LinkedIn scaping tool that captures message urls, conversations from message threads, and profile urls. This tool uses python, selenium, chromedriver and is deployed in a docker container using the [joyzoursky/docker-python-chromedriver image](https://github.com/joyzoursky/docker-python-chromedriver).

This is a super simple tool with all functions in one file: run_scraper.py.

## Instructions for setting up docker

1) Download Docker from [docker.com](https://www.docker.com/get-started) using the 'Download desktop and take a tutorial option'

2) Create a free account and log in on the website

3) When you execute the app on your desktop, you will see the a whale/ship icon on your top bar with moving boxes. This tells you it's loading. When it's done, make sure you are logged in by clicking on the icon. It should have your name:sign out. You will need to be logged in to build images and run containers.

## File Structure

1) Clone this scraper repository

2) Then cd into the directory that you cloned the repository into

```

    $ cd /path/to/folder/you/want

    $ ls 
	
    On your local machine, you should see the app folder, Dockerfile, and requirements.txt. 
```

3) It is very important that the Dockerfile and requirements.txt is one folder up from app. Docker builds the image with the Dockerfile and requirements.txt. When you run the container, it will contain everything from the app folder down and not include the app folder itself.

## Data Information

Scraped information is put into 2 csv's in app/data 
	
1) Who viewed profile csv fields: profileurl, first name, last name of people who viewed the profile
	
	```
	{login_name}.viewerinfo.csv
	```
	
2) Message information csv (from the message tab) has the fields: profile url, first name, last name, full message thread, message url 

	```
	{login_name}.messages.csv
	```
 
 ## Command Line Instructions


1) Build the image on your local machine. You will only need to do this once. 



	```
	$ docker build -t scraper . 
	```

	Note: 
	scraper = name of the image that you will make containers from. Name this whatever you like.
	
	. = the current directory. Docker will look for the Dockerfile in the directory you are in, so it is important you 	start in the right place.

2) Make a container using the built image

	```

	$ docker run -it -w /usr/workspace -v /path/on/your/local/machine:/usr/workspace scraper bash

	```

	This opens up a terminal IN the container that was created. From here you can run the script just as you would from your local machine. 

3) Type in the command line of the container to collect data (in the 2 csv's listed above) and placed in data/

	```
	# python run_scrape.py "username" "password"

	```

## More Useful Docker Commands 

You can find a nice, comprehensive list of docker commands [here](https://www.linode.com/docs/applications/containers/docker-commands-quick-reference-cheat-sheet/)

The ones I use all the time are:

```
	$ docker ps

	Lists all running containers
```

```
	$ docker images

	Lists all images on local machine
```

```
	$ docker stop [container name or ID]

	Stops the container
```


