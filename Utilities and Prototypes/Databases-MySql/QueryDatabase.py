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
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
	

try:
#    while True:
#        Temperature=str(read_temp())
#        print(Temperature)
#        curs.execute ("""INSERT INTO tempdat 
#            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'kitchen', Temperature)""")
#        db.commit()
#        time.sleep(1)

	curs.execute ("SELECT * FROM tempdat")
	print "\nDate     	Time		Zone		Temperature"
	print "==========================================================="

	for reading in curs.fetchall():
		print str(reading[0])+"	"+str(reading[1])+" 	"+reading[2]+"  	"+str(reading[3])

except Exception, e:
    db.close()
    print "Error: the database is being rolled back"
    db.rollback()
    raise e


