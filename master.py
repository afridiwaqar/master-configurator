#!/bin/python

import os, sys, inspect
import getpass
import imp
import argparse

__author__ = 'Muhammad Waqar Afridi'

module_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"modules/")))

parser = argparse.ArgumentParser(
	description='Create configuration based on your system Specs')

parser.add_argument(
	'-a', '--all', help='Find all existing CONFs in system and replace them with newer ones depanding on my system', action='store_true')
parser.add_argument(
	'-c', '--conf', type=str, help='The Conf file you want to generate')
parser.add_argument(
	'-f', '--find', help='Find all the conf files on my system', required=False, default=None, action='store_true')
parser.add_argument(
	'-s', '--show', help='Show all the availble modules with master-configurator', required=False, default=None, action='store_true')

# Array for all arguments passed to script

if len(sys.argv) < 2:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

def system_confs():
	
	system_configs = []
	
	for root, dirs, files in os.walk("/"):
		for file in files:
			if file.endswith('.conf'):
				system_configs.append(file)
				a =  root +"/"+file
				system_configs.append(a)

	return system_configs

def getVarFromFile(configuration_path):

	filename = ''
	filepath = ''
		
	if configuration_path not in sys.path:
		sys.path.insert(0, configuration_path)

		import configuration
		
		filename = configuration.configfile
		filepath = configuration.path

		del sys.modules['configuration']

	return filepath, filename
	
def available_confs():	
	available_configs = []
	module_config_path = []
	confignames = []
	for child in os.listdir(module_path):
		config_path = os.path.join(module_path, child)
		filepath = ''
		if os.path.isdir(config_path):
			filepath, filename = getVarFromFile(config_path+"/")
			a = filepath +"/"+ filename
			available_configs.append(a)
			module_config_path.append(config_path)
			confignames.append(filename)
	return available_configs, module_config_path, confignames

if args.all:
		
	print "Please Wait! Searching for all the confs on the system and generating configurations accordingly for the following configs\n"
	confs_sys = system_confs()
	total_return = available_confs()
	
	confs_avail = total_return[0]
	
	conf_index_str = ''
	index_no = 0
	for each_conf in total_return[0]:
		conf_index_str += str(each_conf)+"_"+str(index_no)+","
		index_no = index_no+1

	search_list = str(conf_index_str).split(',')
	module_conf_path = total_return[1]
	
#	confs_avail_a, module_conf_path, confignames = available_confs()
	
	a = str(set(confs_sys) & set(confs_avail))

	val_set = eval(a)

	for element in val_set:
		conf = os.path.basename(element)
		module_path = ''
		if search_list:
			for each_str_path in search_list:
				index_split = str(each_str_path).split('_')
				if index_split[0]==element:
					found_index = int(index_split[1])
					module_path =total_return[1][found_index]
					break
		configuration_path = module_path
		if configuration_path not in sys.path:
			sys.path.insert(0, configuration_path)
			import configuration
			configuration.gen_all()
#			sys.path.remove(configuration_path)
#			del configuration
			del sys.modules['configuration']
			

if args.conf:
	print "\nplease wait a conf file is generated...\n"
	configuration_path = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"modules/"+str(args.conf))))
	print configuration_path
	if configuration_path not in sys.path:
		sys.path.insert(0, configuration_path)
		import configuration
		configuration.gen_all()
		#sys.path.remove(configuration_path)
		#del configuration
		del sys.modules['configuration']

if args.find:
	print "\nSearching for all the confs on the system...\n"
	confs = system_confs()
	print '\n\n'.join(confs) + '\n'

if args.show:
	print "\nThe Available modules are...\n"
	confs, paths, names = available_confs()
#	print '\n\n'.join(confs) + '\n'
#	print '\n\n'.join(names) + '\n'
#	print '\n\n'.join(paths) + '\n'
	for path in paths:
		print os.path.basename(path)+"\n"
	



