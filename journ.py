#! python3

from sys import stdin
import datetime
import os

# contains the body of the journal entry
content = ""

# takes input from user till EOF
for line in stdin:
	content+=line

# finds current date
current_date = datetime.date.today()

# converts date into a string
date_string = "{}-{}-{}".format(current_date.year,current_date.month,current_date.day)

# opening the filestream for the journal entry
fhand = open(date_string+".txt",'a')

# checking if file is empty aka if file exists
if os.stat(date_string+".txt").st_size==0:
	# writing the date and the content to the file
	content = "Date: " + date_string + "\n" + content
else:
	# line break if the file isn't empty
	content = "\n"+content

# final writing
fhand.write(content)

# closing the file stream
fhand.close()