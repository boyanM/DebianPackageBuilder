#!/usr/bin/python3

import json
import os
import default_params

x = '{ "name":"deb_test", "version":"2", "arch":"all", "maintainer":"tb", "size":"12MB", "depen":"nginx", "section":"nginx", "priority":"optional", "homepage":"https://metacpan.org", "desc":"This is Description", "long_desc":"This is Long Description" }'

json_test = """
{
   "name":"deb_test",
   "version":"2",
   "arch":"all",
   "maintainer":"tb",
   "size":"12MB",
   "depen":"nginx",
   "section":"nginx",
   "priority":"optional",
   "homepage":"https://metacpan.org",
   "desc":"This is Description",
   "long_desc":"This is Long Description"
}
"""

def prepareControlFile(json_request):
	json_params = json.loads(json_request)
	
	deb_dir = os.path.join(
		default_params.PACKAGE_DIRECTORY,
		json_params["name"],
		default_params.CONTROL_DIRECTORY_NAME)

	if os.path.exists(deb_dir):
		print("Go for 500")
	
	else:
		os.mkdir(deb_dir)
	
	control_file = open("{}/control".format(deb_dir),"w")
	control_file_data = []

	control_file_data.append("Package: {}\n".format(json_params['name']))
	control_file_data.append("Version: {}\n".format(json_params['version']))
	control_file_data.append("Architecture: {}\n".format(json_params['arch']))
	control_file_data.append("Maintainer: {}\n".format(json_params['maintainer']))
	control_file_data.append("Installed-Size: {}\n".format(json_params['size']))
	control_file_data.append("Depends: {}\n".format(json_params['depen']))
	control_file_data.append("Section: {}\n".format(json_params['section']))
	control_file_data.append("Priority: {}\n".format(json_params['priority']))
	control_file_data.append("Homepage: {}\n".format(json_params['homepage']))
	control_file_data.append("Description: {}\n".format(json_params['desc']))
	control_file_data.append(" {}\n".format(json_params['long_desc']))

	control_file.writelines(control_file_data)

prepareControlFile(json_test)

