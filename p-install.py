import sys
import json
import zipfile

# print(str(sys.argv))

# default values

configFile = open("config.json", "r")
configArray = json.loads(configFile.read())


# zipObj = zipfile.ZipFile(zip_path)
# for file in zipObj.namelist():
# 	if file.startswith('prestashop/'):
# 		zipObj.extract(file, 'C:\\Users\\gladius882\\test')
# zipObj.close()


# print(var)