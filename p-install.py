from functions import *
import sys

# if isAdmin() == False:
# 	print("Hey! I need admin privileges to do my job!")
# 	sys.exit(-1)

config = getConfiguration()

# virtualHostAdd(config['vhost'])
# createWWWFolder(config['vhost']['DocumentRoot'])

unzip(config['zip_path'], "C:\\Users\\gladius882\\Desktop\\test" )

# unzip(
# 	configArray['zip_path'],
# 	'C:\\Users\\gladius882\\Desktop\\test'
# )