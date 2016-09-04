#Fishtank controller :tropical_fish:

## Description

My name is Juan and I have a 120liter fish tank. I am, however, also an engineer, the lazy type. Fish tanks require quite a lot of work, which includes air pumps, lights, heating and water filtering. As an engineer, I have asked myself: how could I make the fish tank control easier? This is how I got to the idea of an automated fish tank control, which can be operated remotely via a mobile phone app. 

This project uses a Raspberry Pi model B as a main controller. The raspberry Pi is the bridge between the mobile-friendly web application and the fish tank. The development at the moment allows to activate lights, water filter and the air pump. Version 2 of the project allows to control more elements, such as temperature sensor, a Co2 dispenser, LED lights and a pH sensor. 

The following "ReadMe" is the logbook of the development process. This guide is divided into the development notes, todo lists, tasks done, nice to have and command cheat sheet stuff, and helpful notes to have handy in the development process. Towards the end, there is draft version of the installation\rebuilding Wiki, which describes how to rebuild the project again, just in case the system crashes or refuses to work.

If you would like more information regarding my project, feel free to contact me on juanpadillavivas@gmail.com. I would be more than happy to share my experiences with you!

## Version 1 capabilities
* 4 Channels controlling mains socket
* Lights, water pump and air pump control
* Web interface


## Version 2 capabilities(in development)
### Highlights 
New Hardware
* 5 PWM Channels [12V @500 mA] to control lighting
* Temperature sensor [I2C protocol 12bits resolution -55 to 125
* Pressure sensor [max 5bar, Analog output 0 to 5V]
* Uninterruped power supply[battery pack Raspberry pi]
* Electrovalve to control CO2 reactor

Software
* Datalogging Temperature and pressure[Mysql]
* Fishtank scheduled control[Mysql database and webserver]
* External webpage access using IoT
* Active control of CO2 reactor 

System General Arrangement
![Pi SSh console] (https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/Fishtank%20block%20diagram.png "Logo Title Text 1")



Block Diagram
![Pi SSh console] (https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/FT_Controller%20Ver%202.png "Logo Title Text 1")

3D Model 
![Pi SSh console] (https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/VirtualBox_WIN7%20Clone_01_02_2016_23_01_31.png "Logo Title Text 1")

## In Process
* tidy up code
* Decide to use xml files or a DB to log


## ToDo
* Develop script in python to test DB and do Soak test, not required to use the FT2 system, to be done in PI Zero
* DB:
	* Table for configurations (times when outputs need to be activated)
	* Table to log actions
	* Table to log temperature, pressure and output states.
* Implement gauges to show sensors

## NICE TO HAVE
*One macro that reads two independent buttons and controls one output. The output number should be pass a a part of the macro parameters. This will allow to use only one macro for the four outputs.
* Arduino PWM fade slowly lights
* Auto/Manual buttons in the webpage

##Done
* Implement PWM outputs in Arduino
* integrate arduino to the webio
* Full soak test from webio:
* 	Test Temperature
* 	Test Relay Board
* 	Test Pressure and Light board - Arduino
* 	Test webIO
* Wire connectors
* Soak test light board sensor and relay
* Finalise communication arduino RPi
* Test uninterrumped power bank= Succesful, works for less than 45min
* Wire relay mains out of the control box
* Verify Box CAD diagram is still applicable and the holes coincide with the ports of the pi and arduino
* Drill holes and wire db9s
* Finish wiring back plate
* Update the wiring diagram and add to ReadMe file
* Buy connectors JST connectors 2 poles/3 poles//Should arrive by the 2 Apr
* Test temperature sensor
* Connect power to arduino and communicate from Pi
* There is no need to expand the SD memory to use the Pi.
* Wire temperature sensor
* Test relay board
* Buy connectors JST connectors 2 poles/3 poles
* Test waved with the live system.
* Pi-stop lights
* Tidy up ReadMe, grammar and typos.
* Verify database connectivity.
* Change the outputs and Go life Beta version. pins 23,24,25 , temperature sensor addes
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



### Comments-Hot
Images under buttons [link](https://groups.google.com/forum/#!topic/webiopi/URkwd1O42YI), waiting for new realise of webiopi server.


### Past Comments-Cold
read gpio status to html text  https://groups.google.com/forum/#!searchin/webiopi/macro$20LightStatus/webiopi/ho7N8AoOeWo/xULL5L0xZO0J
Changes can be done offline.





##Commands Cheatsheet
Command | Application | Description
------------ | -------------| -------------
git add .| Github|Stages all the changes making them ready to commit
git commit -m "Comment"|Github|insert comments
git push origin master|Github| Push Baby Push commits 
git pull origin master|Github|pull stuff from the git servers, used for updating the local folders
sudo webiopi -d -c /etc/webiopi/config|WebIO|Run server in dev mode
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
sudo nano /etc/webiopi/config |WebIO| configuration of the webio server
cat /proc/cpuinfo|WebIO|See version of the PI
sudo /etc/init.d/webiopi start|Linux| starts the server without console debuger
sudo /etc/init.d/webiopi stop|Linux| stops webio server 
ssh-keygen -R <host>|Linux| When ssh remote identification has changed


##Links
Description | Link
------------ | -------------
Github markdown cheat sheet | https://guides.github.com/features/mastering-markdown/
Webio webpage |https://code.google.com/p/webiopi/
WEbio JavaScript Library|https://code.google.com/p/webiopi/wiki/JAVASCRIPT
SW Engineering course |https://www.udacity.com/course/software-development-process--ud805
Webio tutorial with bacon |http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/
Getting started with GITHub|http://www.instructables.com/id/Introduction-to-GitHub/?ALLSTEPS
Database tutorial |http://raspberrywebserver.com/sql-databases/using-mysql-on-a-raspberry-pi.html

Welcome to the Fishtank wiki!


## Bill of Materials
Item | Description| Reference | Link 
------------ | -------------| -------------| -------------
Raspberry Pi| Single Board Computer that control the system|development version 0003 Q3 2012 B (ECN0001) 1.0 256MB| RS components obsolete now
Temperature sensor| measures the fishtank temperature| DS18B20|[Link]( http://socomponents.co.uk/shop/ds18b20-waterproof-digital-probe-temperature-sensor-thermometer-thermal-module)
Relay board 8 channel| Actuator of the system, switches 240 V| Relay board compatible with Raspberry Pi  |[Link](http://socomponents.co.uk/shop/5v-dc-eight-8-channel-relay-module-for-arduino-raspberry-pi-pic-avr)
Socket lead | Socket switchable from system| 4 Way switchable multiadaptor with 2 usb ports |[Link](http://www.ebay.co.uk/itm/271422236758)
Enclosure | Waterproof box used to host the system | IP65 Enclosure 250x190x80mm clear lid |[Link]( http://www.ebay.co.uk/itm/161873158432)


#Software Installed:

Software | Description| Link
------------ | ------------- | -------------
|headless pi| SSH  | Mac handles it from the terminal
|remote connection|Netatalk | http://gettingstartedwithraspberrypi.tumblr.com/post/24398167109/file-sharing-with-afp-and-auto-discovery-with
|WebIO Pi|0.7.1 (02/10/15)|http://webiopi.trouch.com/DOWNLOADS.html
------------ | ------------- | -------------

#Version
2A

## References

Description | Link
------------ | -------------
Github markdown cheat sheet | https://guides.github.com/features/mastering-markdown/
Webio webpage |https://code.google.com/p/webiopi/
JavaScript Library|https://code.google.com/p/webiopi/wiki/JAVASCRIPT
Sw development course |https://www.udacity.com/course/software-development-process--ud805
webio tutorial with bacon |http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/


#Telling the story
The following steps summarise the process of setting up the raspberry pi for the development of the Fish tank project

##1 Setting up Rasp pi from scratch

I don’t really have spare screens keyboards and mice kicking around my place, therefore I had to learn how to communicate with the Raspberry Pi(Here after “Pi”) using SSH. This is called “Raspberry headless"
The first thing to do is to find the IP address of the PI. To do so, connect to the internet access point at home(Router) and find who is connected to it. Then open a terminal: in Mac this is done by pressing ⌘+space and then type “terminal” and press Enter.  When in the terminal, type ssh pi@192.168.1.7 (use your own ip address, this is an example that worked in my case). Finally, enter your password, which is usually raspberry

	```
	ssh pi@192.168.1.7
	```
Then enter your password, usually is raspberry 


![Pi SSh console](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/SmallSize/Pi%20SSh%20Small.png "Logo Title Text 1")

Voila!!!, You are now in the command prompt of the Pi. From here everything should be easier, if you know what I mean.. It is recommendable to update the  Pi software the first time it is connected (I am assuming an internet connection is available).  
	
	```
	sudo apt-get update 
	sudo apt-get upgrade 
	sudo apt-get autoremove
	```
	
For more information go to: https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=74176

##2 Making the Pi environment confortable to play with:
The following applications will make the linux enviroment easier to edit, test and run applications.
###File sharing AFP 
This application allows to open the directories of the PI as they were “Living” local in your mac. To do so, it is necessary first to install the Netatalk in the Pi.. To do so, enter the following command in the shell 
	```
	sudo apt-get install netatalk
	```

Having installed the netatalk in the Pi, you need to access the RasperryPi, to do so press ⌘ + k 
For more information click on the [link] (http://gettingstartedwithraspberrypi.tumblr.com/post/24398167109/file-sharing-with-afp-and-auto-discovery-with)

Connection

![Net talk server connection](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/Pi%20Nettalk%20Server%20connection.png "Logo Title Text 1")

Password validation

![Password validation](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/Pi%20Net%20talk%20server%20validation.png "Logo Title Text 1")

Pi directory

![Pi home directory](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/Pi%20Home%20directory.png "Logo Title Text 1")

		
###Installing a script editor

Once Netatalk has been installed, you can access files that are in the Pi and edit them locally as if they were on your own computer. That is just brilliant (and also really handy)! Now you need a good text editor. My weapon of choice is Sublime. According to Wikipedia, "Sublime is a cross-platform text and source code editor with a Python application programming interface (API). It natively supports many programming languages and markup languages, Sublime Text is proprietary software; all license revenue accrues to the developer." If you have the means, please buy it and support the team. It is a really good application. It can be used as a trial for a while.


Sublime

![Sublime 2 editor](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/PI%20Sublime%20screenshot.png "Logo Title Text 1")


##3 Installing webIO

WEbIO Pi is a really good approach to the internet of things. This framework allows to control, debug and use the RaspberryPI GPIO from any webpage. Moreover, it is equipped with a set of sensor/actuator libraries and plugins that facilitates the communication with standard sensors.

WEBIO framework

![Web io framework](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/webiopi-framework.png "Logo Title Text 1")

For more information how to install and examples go to the following links
http://webiopi.trouch.com/INSTALL.html

http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/

##4 Hello world web
The first and essential step into the internet of things is to control a single output, to do so, the following link provides a step by step lifesaver tutorial.


http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/

##5 working around with the interface
![Hello cruel wordl of IOT](https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/First_Application_Version.png "Logo Title Text 1")


##6 Circuit layout
![GitHub Logo] (https://github.com/FreeRangeLobster/Fishtank_Development/blob/master/ScreenGrabs%20and%20Pics/Fishtank%20controller%20electrical%20diagram.png)


To Add in the readme, needs a bit of tidy up:

#Using windows to prepare SD card: 
Windows format SD card:  [Link] (https://www.raspberrypi.org/forums/viewtopic.php?f=26&t=13138)
Flash image:  [link](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md)



#pi semaphore GPIO positions

Item | Description| Reference | Link |Position|Pin|Colour
---------|----------|------------|------------|------------|------------|
Close to the border|GPIO7|Red
	|GPIO8|Amber
	|GPIO25|Green
Other side:
	|GPIO10|Red
	|GPIO9|Amber
	|GPIO11| Green

#Temperature one wire support
get into the configuration folder to add the sensor in the boot 
	
	
```
sudo nano /boot/config.txt
```
 in the last line  add 
```
dtoverlay=w1-gpio
```
reboot the pi

```
sudo reboot
```
find the serial of the sensor by typing in the terminal
```
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls
```

Copy the serial of the sensor that starts with
 
```
28-xxxx  
```

Enter to the configuration of the web server using the following command
```
sudo nano /etc/webiopi/config
```

As always before making any changes save a backup and comment changes in the code. In the device section add the following line of code 

```

...

#temp0 = TMP102
#temp1 = TMP102 slave:0x49
#temp2 = DS18B20
#temp3 = DS18B20 slave:28-0000049bc218

#=============Add this sensor ID ======================
tmp0 = DS18B20 slave:28-04146de39cff
#======================================================

#bmp = BMP085
28-xxxx  
```



then save and reestart the servergo to the webpage and it should show the temperature.


reference [Link](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing/ds18b20)



#setup wifi
```
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
```

Compare the contents of the file, if it exists, to the following code. If the file is empty, you can use this code to populate it. Take note of the commented lines (indicated by the # marks) to reference which variable you should use based on your current Wi-Fi node configuration.

```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
network={
ssid="YOURSSID"
psk="YOURPASSWORD" 

# Protocol type can be: RSN (for WP2) and WPA (for WPA1)
proto=WPA

# Key management type can be: WPA-PSK or WPA-EAP (Pre-Shared or Enterprise)
key_mgmt=WPA-PSK

# Pairwise can be CCMP or TKIP (for WPA2 or WPA1)
pairwise=TKIP

#Authorization option should be OPEN for both WPA1/WPA2 (in less commonly used are SHARED and LEAP)
auth_alg=OPEN
}
```

When you’re done editing the file, press CTRL+X to save and exit the document. Now is the time to unplug the Ethernet cable and plug in the Wi-Fi dongle.

At the command prompt, enter the following command:

```
sudo reboot
```




#Set static ip 
The system will be operated using a mobile, it will be way too difficult to scan the whole network searching for the address that has the application. Therefore, It is an "Deadly important to have" a stati address. In this case the application I use 192.168.1.19. The following command allows to enter to the register:


```
sudo nano /etc/network/interfaces
```

As always, when it comes to modify a register, it is a good practice to take a back up of the configuration. just in case

BackUp wireless configuration
	```
	auto lo
	iface lo inet loopback
	auto eth0
	
	allow-hotplug eth0
	iface eth0 inet manual
	
	auto wlan0
	allow-hotplug wlan0
	iface wlan0 inet manual
	
	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
	
	auto wlan1
	allow-hotplug wlan1
	iface wlan1 inet manual
	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf 
	```

New configuration including the static IP address
	```
	auto lo
	iface lo inet loopback
	iface eth0 inet dhcp
	
	allow-hotplug wlan0
	iface wlan0 inet static
	address 192.168.1.19
	netmask 255.255.255.0
	gateway 192.168.1.1
	wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
	iface default inet dhcp
	```
Reference [Link](http://weworkweplay.com/play/automatically-connect-a-raspberry-pi-to-a-wifi-network/)

After rebooting the system, and attempting to ssh the pi 
```
ssh pi@192.168.1.19
```

If the same address has been used to connect other Pies, the terminal might prompt something like this:

```
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@    WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!     @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
IT IS POSSIBLE THAT SOMEONE IS DOING SOMETHING NASTY!
Someone could be eavesdropping on you right now (man-in-the-middle attack)!
It is also possible that a host key has just been changed.
The fingerprint for the RSA key sent by the remote host is
d4:ae:02:2c:bb:97:b0:38:3f:c1:cd:a8:58:68:d7:55.
Please contact your system administrator.
Add correct host key in /Users/Juan/.ssh/known_hosts to get rid of this message.
Offending RSA key in /Users/Juan/.ssh/known_hosts:8
RSA host key for 192.168.1.19 has changed and you have requested strict checking.
```

To solve this issue type:
```
ssh-keygen -R <host>
```
For my case
```
ssh-keygen -R 192.168.1.19
```

To set the time
```
sudo date -s "Thu Aug  9 21:31:26 UTC 2012"
```
To see the current time

```
date '+%A %W %Y %X'
```

Run program in Python
```
	python <filename>.py
```

#Arduino Fishtank controller commands
Description| Command| Reply 
------------ | -------------| -------------
Arduino Status | S |XXXXX-Pressure*
Channel 1 On|Ch1ON|_Ch1ON
Channel 2 On|Ch2ON|_Ch2ON
Channel 3 On|Ch3ON|_Ch3ON
Channel 4 On|Ch4ON|_Ch4ON
Channel 5 On|Ch5ON|_Ch5ON
Channel 1 Off|Ch1OFF|_Ch1OFF
Channel 2 Off|Ch2OFF|_Ch2OFF
Channel 3 Off|Ch3OFF|_Ch3OFF
Channel 4 Off|Ch4OFF|_Ch4OFF
Channel 5 Off|Ch5OFF|_Ch5OFF

* X: is the state of the output, where 1 is activated and 0 is off
* Pressure: is a 3 digit raw measurement of the pressure



>>>>>>> 84273ea43e8319a94ea1723a8e7c202e5dd7bbd7
