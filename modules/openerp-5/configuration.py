import os
import ConfigParser
import os, sys, inspect

localsystem_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../..")))

if localsystem_path not in sys.path:
	sys.path.insert(0, localsystem_path)

import localsystem

configfile = "openerp-server.conf"
path = '/etc'
full_path = path + configfile

def gen_config():
	
#	if not os.path.isfile(full_path):
	# Create the configuration file as it doesn't exist yet
	cfgfile = open(full_path, 'w')
	
	# Add content to the file
	Config = ConfigParser.ConfigParser()
	Config.add_section('options')
	Config.set('options', 'assert_exit_level', 'warn')
	Config.set('options', 'server_actions_allow_code', 'False')
	Config.set('options', 'secure', 'False')
	Config.set('options', '--cache-timeout', '100000') #default
	Config.set('options', 'secure_pkey_file', 'server.pkey')
	Config.set('options', 'netinterface', localsystem.active_interface)
	Config.set('options', 'admin_passwd', 'admin')
	Config.set('options', 'demo', '')
	Config.set('options', 'login_message', 'Welcome to OpenERP on ' + str(localsystem.hostname))
	Config.set('options', 'db_maxconn', '64') #Find Proper Value
	Config.set('options', 'reportgz', 'False')
	Config.set('options', 'xmlrpc', 'True')
	Config.set('options', 'db_port', 'False')
	Config.set('options', 'debug_mode', 'False')
	Config.set('options', 'logfile', '/var/log/openerp-server/erp.log')
	Config.set('options', 'csv_internal_sep', ',')
	Config.set('options', 'translate_modules', "['all']")
	Config.set('options', 'stop_after_init', 'False')
	Config.set('options', 'email_from', 'False')
	Config.set('options', 'addons_path', '/usr/local/lib/python2.7/dist-packages/openerp-server/addons')
	Config.set('options', 'without_demo', 'False')
	Config.set('options', 'netport', '8070')
	Config.set('options', 'syslog', 'False')
	Config.set('options', 'list_db', 'True')
	Config.set('options', 'port', '8069')
	Config.set('options', 'log_level', 'info')
	Config.set('options', 'smtp_port', '25')
	Config.set('options', 'smtp_server', 'localhost')
	Config.set('options', 'db_user', localsystem.current_user)
	Config.set('options', 'price_accuracy', 3)
	Config.set('options', 'import_partial', '')
	Config.set('options', 'soap', 'False')
	Config.set('options', 'pidfile', 'None')
	Config.set('options', 'smtp_password', 'False')
	Config.set('options', 'secure_cert_file', 'server.cert')
	Config.set('options', 'interface', localsystem.active_interface)
	Config.set('options', 'pg_path', 'None')
	Config.set('options', 'root_path', '/usr/local/lib/python2.7/dist-packages/openerp-server')
	Config.set('options', 'smtp_user', 'False')
	Config.set('options', 'db_name', 'False')
	Config.set('options', 'db_host', 'False')
	
	Config.write(cfgfile)
	cfgfile.close()
	print configfile + " Done"

def gen_all():
	gen_config()
