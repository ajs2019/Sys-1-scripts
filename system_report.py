#!/usr/bin/python3
#Adam Stout NSSA 221
#9/17/2022


import os
import platform
os.system('clear')

hostname = platform.node()
uname = os.popen('whoami').read().rstrip()
filename = "/home/" + uname + '/' + hostname + "_system_report.log"

f = open(filename, 'w')


#(DEVICE INFORMATION)

f.write('Device Information\n')
print('Device Information')

#hostname
print('Hostname:\t\t'+ hostname)
f.write('Hostname:\t\t'+ hostname + '\n')

#domain
domainname = os.popen('domainname').read()

f.write('Domain:\t\t\t'+ domainname +'\n')
print('Domain:\t\t\t'+ domainname)




#(NETWORK INFORMATION)

f.write('Network Information\n')
print('Network Information')

#ip
ip = os.popen("ip a s ens192 | awk '/inet / {print $2}' | cut -d/ -f1").read()

f.write('IP Address:\t\t' + ip)
print('IP Address:\t\t' + ip, end ='')


#gateway
gateway = os.popen("ip r | awk ' /^def/{print $3}'").read()

f.write('Gateway:\t\t' + gateway)
print('Gateway:\t\t' + gateway, end='')


#netmask
netmask = os.popen("ifconfig | grep netmask | awk '{print $4}' | sed '3d;2d'").read()
 
f.write('Network Mask:\t\t' + netmask)
print('Network Mask:\t\t' + netmask, end='')

#DNS
with open('/etc/resolv.conf', 'r') as d:
	next(d)
	next(d)
	for index, i in enumerate(d):
		line = i.split(" ")
		index += 1
		print("DNS" + str(index) + ":\t\t\t" + line[1], end = '')
		f.write("DNS" + str(index) + ":\t\t\t" + line[1])	
f.write('\n')




#(OS INFOMATION)

f.write('OS Information')
print('\nOS Information')

#Operating system and version 
with open('/etc/os-release', 'r') as e:
	for index, i in enumerate(e):
		lines = i.split('"')
		if index == 0:
			f.write("\nOperating System:\t" + lines[1])
			print("Operating System:\t" + lines[1])
		if index == 4:
			f.write("\nOperating Version:\t" + lines[1] + '\n')
			print("Operating Version:\t" + lines[1])
#Kernal version
f.write("Kernal version:\t\t" + platform.release() + '\n\n')
print("Kernal version:\t\t" + platform.release())




#(STORAGE INFORMATION)
f.write('Storage Information\n')
print('\nStorage Information')

#capacity
capacity = os.popen("df -BG | grep root | awk '{print $2}'").read()

print("Hard Drive Capacity:\t" + capacity, end = '')
f.write("Hard Drive Capacity:\t" + capacity)

#avaible 
avaliable = os.popen("df -BG | grep root | awk '{print $4}'").read()

print("Avaliable Space:\t" + avaliable)
f.write("Avaliable Space:\t" + avaliable + '\n')




#(CPU INFOMATION)

print('Processor information')
f.write('Processor Information\n')

#CPU model
model = os.popen("cat /proc/cpuinfo | grep 'model name' | awk '{print $4,$5,$6,$7}' | sed '2d'").read()
print("CPU Model:\t\t" + model, end='')
f.write("CPU Model:\t\t" + model)

#Processor count
proccount = os.popen("cat /proc/cpuinfo | grep 'processor' | wc -l").read()
print("Number of processors:\t" + proccount, end ='')
f.write("Number of processors:\t" + proccount)

#CPU cores
cores = os.popen("cat /proc/cpuinfo | grep 'cpu cores' | awk '{print $4}' | sed '2d'").read()
print("Number of cores:\t" + cores)
f.write("Number of cores:\t" + cores + '\n')




#(RAM INFOMRATION)

print("Memory Infomration")
f.write("Memory Information\n")

#total RAM
total = os.popen(" free -h | grep 'Mem' | awk '{print $2}'").read()
print("Toal RAM: \t\t" + total, end ='')
f.write("Toal RAM: \t\t" + total)

#Free RAM
free = os.popen(" free -h | grep 'Mem' | awk '{print $7}'").read()
print("Avaliable RAM:\t\t" + free)
f.write("Avaliable RAM:\t\t" + free)

f.close()
