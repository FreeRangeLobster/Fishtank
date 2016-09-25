#!/usr/bin/env python

import MySQLdb


db = MySQLdb.connect("localhost", "monitor", "password", "temps")
curs=db.cursor()

# note that I'm using triplle quotes for formatting purposes
# you can use one set of double quotes if you put the whole string on one line
try:
	curs.execute ("""INSERT INTO tempdat 
            values(CURRENT_DATE(), NOW() - INTERVAL 12 HOUR, 'kitchen', 20.6)""")
	db.commit()

	print "After Commit"
	curs.execute ("SELECT * FROM tempdat")
	print "\nDate     	Time		Zone		Temperature"
	print "==========================================================="

	for reading in curs.fetchall():
		print str(reading[0])+"	"+str(reading[1])+" 	"+reading[2]+"  	"+str(reading[3])


except:
   print "Error: the database is being rolled back"
   db.rollback()