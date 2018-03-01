import os, sys, inspect
import getpass
import socket
import netifaces
import subprocess
import multiprocessing
from psutil import virtual_memory

current_user =  getpass.getuser()

#print "Getting System Name"
hostname = socket.gethostname()
#print hostname

#print "Getting Active Interface..."
active_interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
#print active_interface

#print "Getting Active Interface Mac address"
macaddr = netifaces.ifaddresses(active_interface)[netifaces.AF_LINK][0]['addr']
#print macaddr

#print "Getting System IP"

local_ip = subprocess.check_output("ip addr | grep 'state UP' -A2 | tail -n1 | awk '{print $2}' | cut -f1  -d'/'", shell=True).strip()
#print local_ip

public_ip_address = socket.gethostbyname(hostname)
#print public_ip_address

#print "Getting System Process Information"
no_of_processors = multiprocessing.cpu_count()
#print no_of_processors
#processor_speed = 

#print "Getting System Memory"
mem = virtual_memory()
ram = mem.total
#print ram
