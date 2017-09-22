#! python3

import os
import glob
import re


# list of unorganized files

file_list = glob.glob(os.path.join(".","*.txt"))

for file in file_list:
	file_data = re.findall("(\d*)-(\d*)-(\d*).txt",file)

	try:
		os.makedirs(os.path.join(".",file_data[0][0],file_data[0][1]))
	except FileExistsError:
		pass
	os.rename(file,os.path.join(".",file_data[0][0],file_data[0][1],file[2:]))

