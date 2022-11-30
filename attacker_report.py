#!/usr/bin/python3

from geoip import geolite2 as ip;
import os;

os.system('clear');

date = os.popen("date | awk '{print $2, $3, $6}'").read().rstrip();

print("Attacker Report - " +str(date))

ipUnique = [];
ipCount = [];
count = 1;


with open('syslog.log') as f:
	for line in f:
		try:
			newline = line[line.index("Failed password for root from") + len("Failed password for root from"):];
			
			newline = newline.strip().split();
			
			ipAddress = newline[0];
			

			if ipAddress not in ipUnique:
				ipUnique.append(ipAddress);
				

			ipCount.append(ipAddress);
			
		except:
			counter = 0; 
	
	
	
	print ("\nCount       IP        Location    \n-----    ---------    --------");
	try:
		while True: 
			
			count += 1;
			
			ipAddress = str(ipUnique[count])
			
			match = ip.lookup(ipAddress)
			
			print (str(ipCount.count(ipUnique[count])) + "\t" + str(ipUnique[count]) + "\t" + match.country);
			
	except: 
		counter = 0; 

