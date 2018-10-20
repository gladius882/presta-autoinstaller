import sys
import zipfile

# print(str(sys.argv))

# default values
zip_path = 'D:\\prestashop_1.6.1.18.zip'
www_path = 'C:\\xampp\\htdocs'

domain = 'http://presta.com'
db_server = 'localhost'
db_name = 'presta'
db_user = 'root'
db_password = ''


zipObj = zipfile.ZipFile(zip_path)
for file in zipObj.namelist():
	if file.startswith('prestashop/'):
		zipObj.extract(file, 'C:\\Users\\gladius882\\test')
zipObj.close()


# print(var)