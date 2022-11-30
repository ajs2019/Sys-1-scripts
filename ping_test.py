#!/usr/bin/python3

#Adam Stout
#9/9/2022
#NSSA 221

import os
import subprocess

os.system('clear')

print('Enter Selection:\n')

print('1 - Test connectivity to your gateway')
print('2 - Test for remote connectivity')
print('3 - Test for DNS resolution')
print('4 - Display default gateway IP address\n')

num = input('Please enter a number: ')
num = int(num)


# checks for incorrect input
while int(num) < 1 or int(num) > 4:
	print ('Number must be between 1 and 4\n')
	num = input('Please enter a number: ')
	num = int(num)

#Tests gateway connection (stores gateway via a command)
if num == 1 :

	print("\nTesting connectivity to the gateway...\n")
	
	gateway = os.popen("ip r | awk ' /^def/{print $3}'").read()

	if subprocess.call("ping -c 1 " + str(gateway) , stdout=subprocess.PIPE, stderr=subprocess.PIPE,  shell=True) == 0 :
		print('Connection Success!') 
	else:
		print('Connection Failed!')

#Tests remote conenction
if num == 2:
	print("\nTesting for remote connectivity...\n")

	if os.system("ping -c 1 129.21.3.17 > /dev/null 2>&1") == 0:
		print("Connection Success!")
	else: 
		print("Connection Failed!")

#Tests DNS resolution
if num == 3:
	print("\nTesting DNS resolution...\n")

	if os.system("ping -c 1 www.google.com > /dev/null 2>&1") == 0:
		print("Connection Success!")
	else: 
		print("Connection Failed!")

#Displays gateway address (stores gateway via a command)
if num == 4 :
	gateway = os.popen("ip r | awk ' /^def/{print $3}'").read()

	print('\nYour default gateway is IP address ' + str(gateway))


	
