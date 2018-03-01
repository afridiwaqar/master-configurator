import os
import inspect
import sys

localsystem_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../..")))

if localsystem_path not in sys.path:
	sys.path.insert(0, localsystem_path)

import localsystem

configfile = "user.rules"
path = '/etc/ufw'
full_path = path + configfile

def gen_config():
	
	print "beginning to make Conf"
	
	# Add content to the file
	os.system('ufw logging on')
	
	print "Default: deny incoming"
	os.system('ufw default deny incoming')

	#Allow by default all outgoing
	print "Default: allow outgoing"
	os.system('ufw default allow outgoing')

	#SSH
	print "Allow SSH"
	os.system('ufw allow 22/tcp')

	#WWW
	print "Allow Web server"
	os.system('ufw allow 80/tcp')

	#FTP
	print "Allow FTP"
	os.system('ufw allow 21/tcp')

	#DNS
	print "Allow DNS"
	os.system('ufw allow 53/tcp')

	#HTTPS
	print "Allow HTTPS"
	os.system('ufw allow 443/tcp')

	#TOR
	print "Allow TOR"
	os.system('ufw allow 9050/tcp')
	os.system('ufw allow 9051/tcp')

	#SMTP
	print "Allo SMTP"
	os.system('ufw allow 25/tcp')

	#POP2/POP3
	print "Allow POP2/POP3"
	os.system('ufw allow 109:110/tcp')

	#SFTP
	print "Allow SFTP"
	os.system('ufw allow 115/tcp')

	#IRC
	print "Allow IRC"
	os.system('ufw allow 194/tcp')

	#IMAP
	print "Allow IMAP"
	os.system('ufw allow 220/tcp')

	#IRCS
	print "Allow IRCS"
	os.system('ufw allow 994/tcp')

	#IRC
	print "Allow IRC"
	os.system('ufw allow 6667/tcp')

	print "Allow postgres"
	os.system('ufw allow postgresql')

	print "Enabling..."
	os.system('ufw enable')
	os.system('ufw reload')

	print configfile + " Done"

def gen_all():
	gen_config()
