import os, ctypes
import json
import zipfile

def isAdmin():
	try:
		is_admin = os.getuid() == 0
	except AttributeError:
		is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

	return is_admin

def getConfiguration(args):
	configFile = open("config.json", "r")
	configArray = json.loads(configFile.read())

	if configArray['vhost']['DocumentRoot'] == '':
		configArray['vhost']['DocumentRoot'] = """%s\\%s""" % (
			configArray['folders']['www_path'],
			configArray['presta']['domain']
		)

	return configArray

def virtualHostAdd(config):
	apacheOutput = '<VirtualHost '+config['ip']+':'+config['port']+'>\n'
	apacheOutput += '\tDocumentRoot "'+config['DocumentRoot']+'"\n'
	apacheOutput += '\tDirectoryIndex '+config['DirectoryIndex']+'\n'
	apacheOutput += '\t<Directory "'+config['DocumentRoot']+'">\n'
	apacheOutput += '\t\tOptions '+config['directory']['Options']+'\n'
	apacheOutput += '\t\tAllowOverride '+config['directory']['AllowOverride']+'\n'
	apacheOutput += '\t\tRequire '+config['directory']['Require']+'\n'
	apacheOutput += '\t</Directory>'+'\n'
	apacheOutput += '</VirtualHost>\n\n'

	with open('C:\\Users\\gladius882\\Desktop\\vhost.txt', 'a') as f:
		f.write(apacheOutput)

def createWWWFolder(path):
	if not os.path.exists(path):
		os.makedirs(path)

def unzip(source, destination):
	zip = zipfile.ZipFile(source)
	for zip_info in zip.infolist():
		if zip_info.filename[-1] == '/' or zip_info.filename.startswith('prestashop/') == False:
			continue
		zip_info.filename = zip_info.filename.replace('prestashop/', '')
		zip.extract(zip_info, destination)
	zip.close()

def restartApache():
	input("Please restart or run Apache service and press Enter to continue")

def createDatabase(db):
	sql = "CREATE DATABASE IF NOT EXISTS `" + db['name'] + '`'
	command = db['mysql_bin'] + " -v --user="+db['user']+" -e \""+sql+"\""
	os.system(command)

def runPrestaInstaller(presta):
	command = ""