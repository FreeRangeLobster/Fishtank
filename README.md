#Fishtank controller :tropical_fish:

## Description

This application is a remote fishtank controller. It was developed on a raspberry pi b+ using WEbio framework which is a great approach to the internet of things. 

## To Do
*Test waved with the live system.
*auto/manual buttons.
*Try writing to a txt.
*Try sensor.
*Documentation of the hardware and bring telling the story back to the md.
*Release project V0 Index.html 
*Go Live in Pi hooked to the fishtank

## In Process
* Implement state indicators, formating colors and text 
* Tide up code and document macros

### Comments-Hot
Changes can be done offline.

### Past Comments-Cold
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
* Implementation on/off indicators
* Save image back up out of the two systems(live one and development projects), can be found in GitHub as Fishtank_live and Fishtank
* Development board connected to waved. 



## NICE TO HAVE
*One macro that reads two independent buttons and controls one output. The output number should be pass a a part of the macro parameters. This will allow to use only one macro for the four outputs.

##Commands Cheatsheet
Command | Application | Description
------------ | -------------| -------------
git add .| Github|Stages all the changes making them ready to commit
git commit -m "Comment"|Github|insert comments
git push origin master|Github| Push Baby Push commits 
git pull origin master|Github|pull stuff from the git servers
Run server in dev mode|WebIO|sudo webiopi -d -c /etc/webiopi/config
sudo su|Linux|super user shell
exit|Linux|to go back to client
./|Linux|run a program
mkdir|Linux|creates a directory
rmdir|Linux|removes a directory
mv <from> <to>|Linux|to move a file, requires the whole addr in the recipient
mv a.jpg b.png|Linux|to move or to rename a file
top	|Linux|to find the number of the process




##Links
Description | Link
------------ | -------------
Github markdown cheat sheet | https://guides.github.com/features/mastering-markdown/
Webio webpage |https://code.google.com/p/webiopi/
JavaScript Library|https://code.google.com/p/webiopi/wiki/JAVASCRIPT
Sw development course |https://www.udacity.com/course/software-development-process--ud805
webio tutorial with bacon |http://forums.connectedly.com/raspberry-pi-f179/how-controlling-gpio-pins-via-internet-2884/
Getting started with GITHub|http://www.instructables.com/id/Introduction-to-GitHub/?ALLSTEPS

