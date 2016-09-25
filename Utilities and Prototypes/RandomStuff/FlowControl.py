import os
import glob
import time
import MySQLdb
 

db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor() 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
Temperature = 1

 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
fin=1
running = 1
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:a]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

def LogTemperature( Temperature, Zone ):
	sql = "INSERT INTO tempdat(tdate, tTime,zone,Temperature) VALUES (CURRENT_DATE(), NOW(), '%s', '%s' )" % (Zone ,Temperature)
	curs.execute(sql)
	db.commit()
	return True 

	

try:
    while running:
        #response = raw_input("Please enter your name: ")
        print "hi"
        time.sleep(1)
        print("This is a good joke")
        print("what happened when the chicken crossed the road")
        gap = raw_input("")
        if gap == (""):
            print("niente")
        else:
            print("")
        print("it died")

        #if raw_input()=="":
        #    option = raw_input("a to stop, b to continue: ")
            #if option== a:
            #   running = 0
        #else:
            #    running = 1
        time.sleep(1)

except Exception, e:
    db.close()
    print "Error: the database is being rolled back"
    db.rollback()
    raise e





#Temperature=str(read_temp())
#        Zone="Office"
#        print(Temperature, Zone)
#        LogTemperature( Temperature, Zone )
        #x = int(raw_input("Please enter an integer: "))
#        time.sleep(1)



#Query database
#	curs.execute ("SELECT * FROM tempdat")
#	print "\nDate     	Time		Zone		Temperature"
#	print "==========================================================="
#
#	for reading in curs.fetchall():
#		print str(reading[0])+"	"+str(reading[1])+" 	"+reading[2]+"  	"+str(reading[3])
# it does work 

#Adding temperature lines to the database

#adding Temperature to the log
#_Temperature=str(read_temp())
#print(_Temperature)
#_tDate= time.time
#_tTime= time.time
#print (time.strftime("%H:%M:%S"))
        #print(_tDate)
#_Zone="Hello"
#print(_Zone)
#sql = "INSERT INTO tempdat(tdate, tTime,zone,Temperature) VALUES ('%s','%s','%s','%s' )" % (_tDate,_tTime,_Zone ,_Temperature)
