import ctypes
import os
import sys
import json
import zipfile

from functions import *

try:
	is_admin = os.getuid() == 0
except AttributeError:
	is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0



# print(str(sys.argv))

# default values

configFile = open("config.json", "r")
configArray = json.loads(configFile.read())

if configArray['vhost']['DocumentRoot'] == '':
	configArray['vhost']['DocumentRoot'] = """%s\\%s""" % (
		configArray['folders']['www_path'],
		configArray['presta']['domain']
	)

VirtualHostAdd(configArray['vhost'])


# zipObj = zipfile.ZipFile(zip_path)
# for file in zipObj.namelist():
# 	if file.startswith('prestashop/'):
# 		zipObj.extract(file, 'C:\\Users\\gladius882\\test')
# zipObj.close()


# print(var)

