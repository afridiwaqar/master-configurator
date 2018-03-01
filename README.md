Master-Configurator is configuration manager that sets applications configuration according to your local system. All the available configurations are written in a modules available under the "modules" folder.
Usage:

If you do not provide any parameter, master-configrator will show help

usage: master.py [-h] [-a] [-c CONF] [-f] [-s]

Create Configuration based on your system Specs

optional arguments:
  -h, --help            show this help message and exit
  -a, --all             Find all existing CONFs in system and replace them with newer ones depanding on my system
  -c CONF, --conf CONF  The Conf file you want to generate
  -f, --find            Find all the conf files on my system
  -s, --show            Show all the availble modules with master-configurator



