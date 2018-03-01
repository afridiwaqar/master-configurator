import os
import ConfigParser
import os, sys, inspect

localsystem_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../..")))

if localsystem_path not in sys.path:
	sys.path.insert(0, localsystem_path)

import localsystem

configfile = "postgresql.conf"
path = '/etc/postgresql/9.5/main'
full_path = path + configfile

def gen_config():

	cfgfile = open(full_path, 'w')

	Config = ConfigParser.ConfigParser()
	Config.add_section('')
	Config.set('', 'data_directory', "'/var/lib/postgresql/9.5/main'")
	Config.set('', 'hba_file', "'/etc/postgresql/9.5/main/pg_hba.conf'")
	Config.set('', 'ident_file', "'/var/run/postgresql/9.5-main.pid'")
	Config.set('', 'external_pid_file', "'/var/run/postgresql/9.5-main.pid'")
	Config.set('', 'listen_addresses', "'*'")
	Config.set('', 'port', '5432')
	Config.set('', 'max_connections', '350')
	Config.set('', 'unix_socket_directories', "'/var/run/postgresql'")
	Config.set('', 'ssl', 'true')
	Config.set('', 'ssl_cert_file', "'/etc/ssl/certs/ssl-cert-snakeoil.pem'")
	Config.set('', 'ssl_key_file', "'/etc/ssl/private/ssl-cert-snakeoil.key'")
	Config.set('', 'shared_buffers', '350MB')
	Config.set('', 'temp_buffers', '64MB')
	Config.set('', 'max_prepared_transactions', '20')
	Config.set('', 'work_mem', '1024MB')
	Config.set('', 'maintenance_work_mem', '1024MB')
	Config.set('', 'dynamic_shared_memory_type', "posix")
	Config.set('', 'effective_cache_size', '4GB')
	Config.set('', 'log_line_prefix', "'%m [%p] %q%u@%d '")
	Config.set('', 'log_timezone', "'localtime'")
	Config.set('', 'cluster_name', "'9.5/main'")
	Config.set('', 'track_counts', 'on')
	Config.set('', 'stats_temp_directory', "'/var/run/postgresql/9.5-main.pg_stat_tmp'")
	Config.set('', 'autovacuum', 'on')
	Config.set('', 'datestyle', "'iso, mdy'")
	Config.set('', 'timezone', "'localtime'")
	Config.set('', 'lc_messages', "'en_US.UTF-8'")
	Config.set('', 'lc_monetary', "'en_US.UTF-8'")
	Config.set('', 'lc_numeric', "'en_US.UTF-8'")
	Config.set('', 'lc_time', "'en_US.UTF-8'")
	Config.set('', 'import_partial', '')
	Config.set('', 'default_text_search_config', "'pg_catalog.english'")
	
	Config.write(cfgfile)
	cfgfile.close()
	
	with open(full_path, 'r') as fin:		# Removing Default Tag and last line blank Tag
		data = fin.read().splitlines(True)
	with open(full_path, 'w') as fout:
		fout.writelines(data[1:-2])

	print configfile + " Done"

def gen_all():
	gen_config()
