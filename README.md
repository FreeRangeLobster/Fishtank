#Fishtank controller :tropical_fish:

## Description

This application is a remote fishtank controller. It was developed on a raspberry pi b+ using WEbio framework which is a great approach to the internet of things. 

## To Do
*Implement state indicators example in  
*Save image back up out of the two systems(live one and development projects)
*auto/manual buttons
*Try writing to a txt
*Try sensor
*waved
*Release project V0 Index.html | 
*Go Live in Pi hooked to the fishtank|

## In Process
*Implementation on/off indicators

### Comments-Hot
read gpio status to html text  https://groups.google.com/forum/#!searchin/webiopi/macro$20LightStatus/webiopi/ho7N8AoOeWo/xULL5L0xZO0J

##Done
* Html layout 
* Edit buttons and reformat	  
* Implementation two bottons routine in all outputs 
* Links to configuration and statistics webpages.
* Status bar.
* Two buttons controlling same output.
* Button On/Off one macro for each output(Not a good practice though) 
* Github subversion

## NICE TO HAVE
*One macro that reads two independent buttons and controls one output. The output number should be pass a a part of the macro parameters. This will allow to use only one macro for the four outputs.

##Commands Cheatsheet
Command | Application | Description
------------ | -------------| -------------
git add .| Github|Stages all the changes making them ready to commit
git commit -m "Comment"|Github|insert comments
git push origin master|Github| Push Baby Push commits 
git pull origin master|Github|pull stuff from the git servers

#Hardware:
4 WAYS MULTI ADAPTOR WITH 2 USB PORTS | http://www.ebay.co.uk/itm/271422236758
8 Channel Relay Module |http://www.ebay.co.uk/itm/271422236758
Raspberry pi reference |xxxxxx

#Software Installed:

Software | Description| Link
------------ | ------------- | -------------
|headless pi|
|remote connection|
||
------------ | ------------- | -------------

#Version

## References

Description | Link
------------ | -------------
Github markdown cheat sheet | https://guides.github.com/features/mastering-markdown/
Webio webpage |https://code.google.com/p/webiopi/
JavaScript Library|https://code.google.com/p/webiopi/wiki/JAVASCRIPT
Sw development course |https://www.udacity.com/course/software-development-process--ud805
webio tutorial with bacon |http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/


#Telling the story
The following steps summarise the process of setting up the raspberry pi for the develpment of the fishtank project

##1 Setting up Rasp pi from scratch

I don’t really have spare screens keyboards and mice kicking around my place, so that I had to learn how to  communicate with the Raspberry Pi(Here after “Pi”) using ssh. this mode of use is called “Raspberry headless"

	https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=74176
	sudo apt-get update 
	sudo apt-get upgrade 
	sudo apt-get auto remove

The first thing to do is to find the IP address of the PI, to do so, connect to the internet accespoint at home, go to find who is connected to the dh

then open a terminal in mac press ⌘+space, 
then type in the terminal 
	ssh pi@192.168.1.3
then enter your password, usually is raspberry 
	

Voila!!!, you are now in the command prompt of the raspberry pi. from here everything should be easier, if you know what I mean …
For more information have a look here:



##2 Making the Pi environment confortable to play with:
File sharing AFP
with this application you can open the directories of the PI as they were “Living” local in your mac. To do so it is needed to install the Netatalk first in the Raspberry pi. enter the following command in the shell
sudo apt-get install netatalk
		
Installing a good  script editor
Install Sublime text if using MAC

##3 Installing webIO
http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/


##4 Hello world web
http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/

##5 working around with the interface
##6 Circuits and connections
##7 Mounting


