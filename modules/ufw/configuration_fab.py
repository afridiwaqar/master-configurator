import os
import inspect
import sys

from fabric.api import *
from fabric.contrib import files

localsystem_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../..")))

if localsystem_path not in sys.path:
	sys.path.insert(0, localsystem_path)

import localsystem

configfile = "user.rules"
path = '/etc/ufw/'
full_path = path + configfile

# Check if there is already a configurtion file


host = '127.0.0.1'
#env.hosts = [host]
env.host_string = host
env.user = 'waqar'
#env.key_filename = "/home/ubuntu/omg.pem"

#localhost= localsystem.current_user + '@' + localsystem.local_ip
#user = localsystem.current_user

@hosts(['localhost'])

def gen_config():
	
#	if not os.path.isfile(full_path):
	print "beginning to make Conf"
	# Create the configuration file as it doesn't exist yet
#	cfgfile = open(full_path, 'w')
	
	# Add content to the file
	sudo('ufw logging on')
	
	print "Default: deny incoming"
	sudo('ufw default deny incoming')

	#Allow by default all outgoing
	print "Default: allow outgoing"
	sudo('ufw default allow outgoing')

	#SSH
	print "Allow SSH"
	sudo('ufw allow 22/tcp')

	#WWW
	print "Allow Web server"
	sudo('ufw allow 80/tcp')

	#FTP
	print "Allow FTP"
	sudo('ufw allow 21/tcp')

	#DNS
	print "Allow DNS"
	sudo('ufw allow 53/tcp')

	#HTTPS
	print "Allow HTTPS"
	sudo('ufw allow 443/tcp')

	#TOR
	print "Allow TOR"
	sudo('ufw allow 9050/tcp')
	sudo('ufw allow 9051/tcp')

	#SMTP
	print "Allo SMTP"
	sudo('ufw allow 25/tcp')

	#POP2/POP3
	print "Allow POP2/POP3"
	sudo('ufw allow 109:110/tcp')

	#SFTP
	print "Allow SFTP"
	sudo('ufw allow 115/tcp')

	#IRC
	print "Allow IRC"
	sudo('ufw allow 194/tcp')

	#IMAP
	print "Allow IMAP"
	sudo('ufw allow 220/tcp')

	#IRCS
	print "Allow IRCS"
	sudo('ufw allow 994/tcp')

	#IRC
	print "Allow IRC"
	sudo('ufw allow 6667/tcp')

	print "Allow postgres"
	sudo('ufw allow postgresql')

	print "Enabling..."
	sudo('ufw reload')

	print configfile + " Done"

def gen_all():
	gen_config()
