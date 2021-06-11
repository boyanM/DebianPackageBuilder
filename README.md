


Structure of debain package:

deb_package
	|
	|  ----- source files ( Name of the file is relative path, but after installation it is translated to absolute)
	|  ----- DEBIAN
		|
		|-----control
		|-----md5sums




Example of DEBIAN/md5sums:
cb1a5000f2d79a5e2b13846e7673bc9f  usr/lib/nginx/modules/ngx_http_vhost_traffic_status_module.so
31a40f2de1f323b23372f018852aa1fb  etc/nginx/modules-enabled/60-status-vts.conf
f3066f67070ab9b1ad9bab81ca05330a  /etc/apache2/sites-available/file.txt 

Example of DEBIAN/control:
Package: deb_test
Version: 2
Architecture: all
Maintainer: tb
Installed-Size: 12MB
Depends: nginx
Section: nginx
Priority: optional
Homepage: https://metacpan.org
Description: This is Description
 This is Long Description
