#! python3

from sys import stdin
import datetime
import os

content = ""

for line in stdin:
	content+=line

current_date = datetime.date.today()

date_string = "{}-{}-{}".format(current_date.year,current_date.month,current_date.day)

fhand = open(date_string+".txt",'a')

if os.stat(date_string+".txt").st_size==0:
	content = "Date: " + date_string + "\n" + content
else:
	content = "\n"+content
fhand.write(content)

fhand.close()