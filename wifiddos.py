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

if len(check_wifi_result) == 0:
	print("please connect a wifi adapter and try again")
	exit()

print("the following wifi interface are available: ")
for index, item in enumerate(check_wifi_result):
	print(f"{index} - {item}")

# ensure the wifi interface selected is valid. simple menu with interface to select form
while True:
	wifi_interface_choice = input("Please select the interface you want to attack >> ")
	try:
		if check_wifi_result[int(wifi_interface_choice)]:
			break
	except:
		print("Please enter a number that corresponds with the choice available")

#for easy reference we call the selected interface hacknic	