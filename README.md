#Fishtank controller :tropical_fish:

## Description

This project started out me being lazy to flicker the switch on and off. I asked myself: What if I control it from my mobile phone? and why not make it automatic?.  Also I have a Raspberry Pi !!!. When I started I thought it was a weekend project, but being here  writing the "ReadMe" of my fishtank controller probes me otherwise. 

The following "ReadMe" is the logbook of the development process, This document is devided into the development notes, to do lists, tasks done, nice to have, comand cheat sheet. 
At the end there is draft version of the project Wiki, which describes how to do it again, just in case the system goes bang.
FYI my mail is juanpadillavivas@gmail.com if you want more information.

 Let's start over again properly: 

My name is Juan, I have a fishtank which I want to control using my mobile phone. The main controller is a Raspberry Pi model B. That single computer board is connected to a driver board which handles the power side of the system.

The raspberry Pi is the bridge between the mobile friendly web application and the fishtank. The development at the moment allows to activate lights, water filter and the air pump. In the future it is intended to go for more elements such as, temperature sensor, Co2 dispenser, LEd lights and PH sensor.

## To Do

* Auto/manual buttons .
* Txt with configuration parameters 
* Investigate if a database is posible to implement
* Add notes about hello world and the first application in the wiki
* Release project V0 Index.html 
* Go Live in Pi hooked to the fishtank and weaved

## In Process
* Change the outputs and Go life Beta version
* Test waved with the live system.
* Pi-stop lights

### Comments-Hot


### Past Comments-Cold
read gpio status to html text  https://groups.google.com/forum/#!searchin/webiopi/macro$20LightStatus/webiopi/ho7N8AoOeWo/xULL5L0xZO0J
Changes can be done offline.


##Done
* Tidy Up application
* formating colors and text 
* Tide up code and document macros
* Test sensor
* Implement state indicators
* Html layout 
* Edit buttons and reformat	  
* Implementation two bottons routine in all outputs 
* Links to configuration and statistics webpages.
* Status bar.
* Two buttons controlling same output.
* Button On/Off one macro for each output(Not a good practice though) 
* Github subversion
* Implementation on/off indicators
* Save image back up out of the two systems(live one and development projects), can be found in GitHub as Fishtank_live and 
Fishtank
* Development board connected to waved. 
* Documentation of the hardware and bring telling the story back to the md.


## NICE TO HAVE
*One macro that reads two independent buttons and controls one output. The output number should be pass a a part of the macro parameters. This will allow to use only one macro for the four outputs.

##Commands Cheatsheet
Command | Application | Description
------------ | -------------| -------------
git add .| Github|Stages all the changes making them ready to commit
git commit -m "Comment"|Github|insert comments
git push origin master|Github| Push Baby Push commits 
git pull origin master|Github|pull stuff from the git servers, used for updating the local folders
Run server in dev mode|WebIO|sudo webiopi -d -c /etc/webiopi/config
sudo su|Linux|super user shell
exit|Linux|to go back to client
./|Linux|run a program
mkdir|Linux|creates a directory
rmdir|Linux|removes a directory
mv <from> <to>|Linux|to move a file, requires the whole addr in the recipient
mv a.jpg b.png|Linux|to move or to rename a file
top	|Linux|to find the number of the process
sudo update-rc.d webiopi defaults |Linux| starts the server on system boot
sudo update-rc.d webiopi remove |Linux| stops starting the server on system boot




##Links
Description | Link
------------ | -------------
Github markdown cheat sheet | https://guides.github.com/features/mastering-markdown/
Webio webpage |https://code.google.com/p/webiopi/
JavaScript Library|https://code.google.com/p/webiopi/wiki/JAVASCRIPT
Sw development course |https://www.udacity.com/course/software-development-process--ud805
webio tutorial with bacon |http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/
Getting started with GITHub|http://www.instructables.com/id/Introduction-to-GitHub/?ALLSTEPS

Welcome to the Fishtank wiki!



#Hardware:
4 WAYS MULTI ADAPTOR WITH 2 USB PORTS | http://www.ebay.co.uk/itm/271422236758
8 Channel Relay Module |http://www.ebay.co.uk/itm/271422236758
Raspberry pi reference |xxxxxx

#Software Installed:

Software | Description| Link
------------ | ------------- | -------------
|headless pi| SSH  | Mac handles it from the terminal
|remote connection|Netatalk | http://gettingstartedwithraspberrypi.tumblr.com/post/24398167109/file-sharing-with-afp-and-auto-discovery-with
|WebIO Pi|0.7.1 (02/10/15)|http://webiopi.trouch.com/DOWNLOADS.html
------------ | ------------- | -------------

#Version
0.02

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

I don’t really have spare screens keyboards and mice kicking around my place, so that I had to learn how to communicate with the Raspberry Pi(Here after “Pi”) using ssh. This mode of use is called “Raspberry headless"

The first thing to do is to find the IP address of the PI, to do so, connect to the internet accespoint at home(Router), go to find who is connected to it. Then open a terminal in mac press ⌘+space, then type in the terminal 
	ssh pi@192.168.1.7
then enter your password, which is usually raspberry 


![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/SmallSize/Pi%20SSh%20Small.png "Logo Title Text 1")

Voila!!!, you are now in the command prompt of the raspberry pi. from here everything should be easier, if you know what I mean It is recomendable to update the SW of the Pi the firstime is connected

	sudo apt-get update 
	sudo apt-get upgrade 
	sudo apt-get auto remove

For more information go to: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=74176

##2 Making the Pi environment confortable to play with:

File sharing AFP 
This application allows to open the directories of the PI as they were “Living” local in your mac. To do so, it is needed to install the Netatalk first in the Raspberry pi. enter the following command in the shell
	sudo apt-get install netatalk
Having installed the netatalk in the Pi, you need to access the rasperryPi, to do so press ⌘ + k 

Connection

![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/Pi%20Nettalk%20Server%20connection.png "Logo Title Text 1")

Password validation

![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/Pi%20Net%20talk%20server%20validation.png "Logo Title Text 1")

Pi directory

![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/Pi%20Home%20directory.png "Logo Title Text 1")

		
Installing a script editor
After having installed the nettalk, you can access files in the pi and edit them locally as if it was in your own computer. that is just brilliant!! and really handy. now you need a good text editor, my weapon of choice is: 
"Sublime is a cross-platform text and source code editor with a Python application programming interface (API). It natively supports many programming languages and markup languages, Sublime Text is proprietary software; all license revenue accrues to the developer." wikipedia
Please if you have the means, buy it, really good application. It can be used as a trial for a while.

Sublime

![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/PI%20Sublime%20screenshot.png "Logo Title Text 1")


##3 Installing webIO

WEbIO Pi is a really good aproach to the internet of things, This framework allows to control, debug and use the RaspberryPI gpio from any webpage. Moreover, it is equiped with a set of sensor/actuator libraries and plugins that facilitates the communication with standard sensors. 

WEBIO framework

![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/webiopi-framework.png "Logo Title Text 1")

For more information how to install and examples go to the following links
http://webiopi.trouch.com/INSTALL.html

http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/

##4 Hello world web
The first and essential step into the internet of things is to control an output, to do so the following link provides an step by step lifesaver tutorial.

http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/

##5 working around with the interface
![alt Logo](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/SmallSize/rsz_1first_application_version.png "Logo Title Text 1")


##6 Circuit layout
![GitHub Logo] (https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/Webio/Screenshoots%20and%20pics/Fishtank%20controller%20electrical%20diagram.png)

