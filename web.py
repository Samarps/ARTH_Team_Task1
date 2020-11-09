import os
import subprocess as sp

def text(c):
	code = "tput setaf " + c
	os.system(code)

# Code for Webserver Configuration:

def web():
	os.system("clear")
	text("2")
	print("\n\t\t\t\tSub-Menu Apache Webserver\n")
	print("\t\t\t\t``````````````````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
	text("3")
	print("1. Configure yum to get httpd software")
	print("2. Configure Apache Webserver (httpd)")
	print("3. Start httpd Services")
	print("4. Stop httpd Services")
	print("5. Permanently enable httpd Services")
	print("6. Permanently disable httpd Services\n")
	text("7")

def web_1():
	os.system("rm -f /etc/yum.repos.d/myyum.repo")
	os.system("echo '[dvd1]' >> /etc/yum.repos.d/myyum.repo")
	os.system("echo 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream'>> /etc/yum.repos.d/myyum.repo")
	os.system("echo 'gpgcheck=0' >> /etc/yum.repos.d/myyum.repo")
	os.system("echo '' >> /etc/yum.repos.d/myyum.repo")
	os.system("echo '[dvd2]' >> /etc/yum.repos.d/myyum.repo")
	os.system("echo 'baseurl=file:///run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS' >> /etc/yum.repos.d/myyum.repo")
	os.system("echo 'gpgcheck=0' >> /etc/yum.repos.d/myyum.repo")
	os.system("clear")
	web()
	text("2")
	print("yum repo is Configured, now you can install or Configure httpd!")
	text("7")

def web_2():
	os.system("yum install httpd -y")
	os.system("systemctl start httpd")
	os.system("clear")
	web()
	text("2")
	print("Apache Webserver Configured & the httpd Service is also Started")
	text("7")

def web_3():
	os.system("systemctl start httpd")
	os.system("clear")
	web()
	text("2")
	print("httpd Services started!")
	text("7")

def web_4():
	os.system("systemctl stop httpd")
	os.system("clear")
	web()
	text("2")
	print("httpd Services stopped!")
	text("7")

def web_5():
	os.system("systemctl enable httpd")
	os.system("clear")
	web()
	text("2")
	print("httpd Services enabled permanently!")
	text("7")

def web_6():
	os.system("systemctl disable httpd")
	os.system("clear")
	web()
	text("2")
	print("httpd Services disabled permanently!")
	text("7")
