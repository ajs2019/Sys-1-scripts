#!/usr/bin/python3
#Adam stout 10/10/2022
#NSSA 221 Script 3 

import sys
import os
import time
import os.path
from os import path

os.system('clear')


while True:
	#Print Menu
	print ("\n('q' to exit the program)\n");
	print ("------Menu-----");	

	print('\n1. Create Shortcut\n2. Delete Shortcut\n3. View Report\n')

	ans = input("Choose an option: ")

	#quit 
	if ans == 'q':
		os.system('clear');
		sys.exit("Exiting the program")
	
	#check for invalid input
	if ans != 'q' and ans != '1' and ans != '2' and ans !='3':
		print("\nInvalid option, please try again")
		time.sleep(3)
		os.system('clear');

		
		
	# Create a Symbolic Link

	if ans == "1":
		os.system('clear');
		# Current directory
		print ("Current directory: " + str(os.getcwd()))

		origin = input("\nAbsolute or Relative path to origin file: ");
		shortcut = input("Give your shortcut a name: ");

 

		# checks if file exists
		if path.exists(origin) == False:
			print("\nFile or Directory does not exist! (Returning To Menu)...\n");
			
			
		else:
			final = input("\nFound " + str(origin) + " Type (Y/y) to add shortcut: ");
			if final == 'y' or final == 'Y':
				os.system("ln -s " + str(origin) + " " + '/home/$USER/' + str(shortcut));
				print('\nShortcut Created Successfully! (Returning To Menu)....\n')
			else:
				print("\nCanceled: Returning to menu...")
		time.sleep(3)
		os.system('clear');


	# Delete a Symbolic Link
	if ans == "2":
		
		os.system('clear');
		# Current directory
		print ("Current directory: " + str(os.getcwd()))

		origin = input("\nEnter the name of the shortcut: ");
		origin = os.popen('echo "/home/$USER/' + str(origin) + '"' ).read().rstrip()

		# checks if file exists and is a symlink
		if os.path.islink(origin) == False:
			print("\nFile is not a shortcut or does not exist! (Returning To Menu)...\n");
				
		else:
			final = input("\nFound " + str(origin) + " Type (Y/y) to comfirm delete: ");
			if final == 'y' or final == 'Y':
				os.system("rm " + str(origin));
				print("\nShortcut Deleted Successfully! (Returning to Menu)... ")
			else:
				print("\nCanceled: Returning to menu...")
		time.sleep(3)
		os.system('clear');

	#View Report
	if ans == "3":

		# Number of symbolic links
		number = os.popen('find /home/$USER -maxdepth 1 -type l -ls | wc -l').read().rstrip()
		

		# Store the Report
		report = os.popen("find /home/$USER -maxdepth 1 -type l | awk -F'/' -v OFS='\n\t\t' '{print  $(NF), $0 }'").read().rstrip()


		# Print the Report
		os.system('clear');
		print ("\nSymbolic Links Summary Report:\n")
		print("Number of Symbolic Links: " + str(number)) 
		print("\nName:\t\tPath:\n--------\t--------" )
		print(str(report))
		input("\nPress ENTER to return to menu: ")
		os.system('clear');
		
		
