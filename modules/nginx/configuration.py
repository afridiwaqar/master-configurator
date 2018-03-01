import os
import ConfigParser
import io, sys, inspect

localsystem_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../..")))

if localsystem_path not in sys.path:
	sys.path.insert(0, localsystem_path)

import localsystem

configfile = "nginx.conf"
path = '/etc/nginx'
full_path = path + configfile

def gen_config():

	cfgfile = open(full_path, 'w')

	Config = ConfigParser.ConfigParser(allow_no_value=True)
	Config.add_section('')
	Config.set('', 'user', "www-data;")
	Config.set('', 'worker_processes', "auto;")
	Config.set('', 'pid', "/run/nginx.pid;")
	Config.set('', 'events', "{")
	Config.set('', 'worker_connections', "1024;")
	Config.set('', 'multi_accept', 'on;')
	Config.set('', '}', '')
	Config.set('', 'worker_rlimit_nofile', "4096;")
	Config.set('', 'http', '{')
	Config.set('', 'sendfile', "on;")
	Config.set('', 'tcp_nopush', "on;")
	Config.set('', 'tcp_nodelay', 'on;')
	Config.set('', 'keepalive_timeout', '10;')
	Config.set('', 'types_hash_max_size', '2048;')
	Config.set('', 'client_body_buffer_size', '128k;')
	Config.set('', 'client_header_buffer_size', '10k;')
	Config.set('', 'client_max_body_size', "10m;")
	Config.set('', 'large_client_header_buffers', '4 256k;')
	Config.set('', 'include', "/etc/nginx/mime.types;")
	Config.set('', 'default_type', "application/octet-stream;")
	Config.set('', 'ssl_protocols', "TLSv1 TLSv1.1 TLSv1.2;")
	Config.set('', 'ssl_prefer_server_ciphers', 'on;')
	Config.set('', 'access_log', "/var/log/nginx/access.log;")
	Config.set('', 'error_log', '/var/log/nginx/error.log;')
	Config.set('', 'gzip', "on;")
	Config.set('', 'gzip_disable', '"msie6";')
	Config.set('', 'include', "/etc/nginx/conf.d/*.conf;")
	Config.set('', 'include', "/etc/nginx/sites-enabled/*;")
	Config.set('', '', '}')

	Config.write(cfgfile)
	
	cfgfile.close()
	
	with open(full_path, 'r') as fin:		# Removing Default Tag and last line blank Tag
		data = fin.read().splitlines(True)
	with open(full_path, 'w') as fout:
#		fout.writelines(data[1:])
		fout.writelines(data[1:-2])

	# Read in the file
	with open(full_path, 'r') as file :
		filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('=', ' ')
	filedata = filedata.replace('   ', ' ')

	# Write the file out again
	with open(full_path, 'w') as file:
		file.write(filedata)

	print configfile + " Done"

def gen_all():
	gen_config()
