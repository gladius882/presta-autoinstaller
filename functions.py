def VirtualHostAdd(config):
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