import os
import ConfigParser
import io, sys, inspect

localsystem_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../..")))

if localsystem_path not in sys.path:
	sys.path.insert(0, localsystem_path)

import localsystem

configfile = "apache2.conf"
path = '/etc/apache2'
full_path = path + configfile

def gen_config():

	cfgfile = open(full_path, 'wb')

	cfgfile.write('Mutex file:${APACHE_LOCK_DIR} default\n')
	cfgfile.write('PidFile ${APACHE_PID_FILE}\n')
	cfgfile.write('Timeout 300\n')
	cfgfile.write('KeepAlive On\n')
	cfgfile.write('MaxKeepAliveRequests 100\n')
	cfgfile.write('KeepAliveTimeout 5\n')
	cfgfile.write('User ${APACHE_RUN_USER}\n')
	cfgfile.write('Group ${APACHE_RUN_GROUP}\n')
	cfgfile.write('HostnameLookups Off\n')
	cfgfile.write('ErrorLog ${APACHE_LOG_DIR}/error.log\n')
	cfgfile.write('LogLevel warn\n')
	cfgfile.write('IncludeOptional mods-enabled/*.load\n')
	cfgfile.write('IncludeOptional mods-enabled/*.conf\n')
	cfgfile.write('Include ports.conf\n')
	cfgfile.write('<Directory />\n')
	cfgfile.write('\tOptions FollowSymLinks\n')
	cfgfile.write('\tAllowOverride None\n')
	cfgfile.write('\tRequire all denied\n')
	cfgfile.write('</Directory> \n')
	cfgfile.write('<Directory /usr/share> \n')
	cfgfile.write('\tAllowOverride None\n')
	cfgfile.write('\tRequire all granted\n')
	cfgfile.write('</Directory>\n')
	cfgfile.write('<Directory /var/www/> \n')
	cfgfile.write('\tOptions Indexes FollowSymLinks\n')
	cfgfile.write('\tAllowOverride None\n')
	cfgfile.write('\tRequire all granted\n')
	cfgfile.write('</Directory>\n')
	cfgfile.write('AccessFileName .htaccess\n')
	cfgfile.write('<FilesMatch "^\.ht"> \n')
	cfgfile.write('\tRequire all denied\n')
	cfgfile.write('</FilesMatch>\n')
	cfgfile.write('LogFormat "%v:%p %h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" vhost_combined\n')
	cfgfile.write('LogFormat "%h %l %u %t \"%r\" %>s %O \"%{Referer}i\" \"%{User-Agent}i\"" combined\n')
	cfgfile.write('LogFormat "%h %l %u %t \"%r\" %>s %O" common\n')
	cfgfile.write('LogFormat "%{Referer}i -> %U" referer\n')
	cfgfile.write('LogFormat "%{User-agent}i" agent\n')
	cfgfile.write('IncludeOptional conf-enabled/*.conf\n')
	cfgfile.write('IncludeOptional sites-enabled/*.conf\n')
	
	cfgfile.close()

	print configfile + " Done"

def gen_all():
	gen_config()
