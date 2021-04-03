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