import os

def text(c):
	code = "tput setaf " + c
	os.system(code)

def instructions():
	text("2")
	print("\t\t\t\t\tWelcome User!\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
	text("3")
	print("I'm your Assistant & I can help you do Configuration related to the following:")
	text("6")
	print("1. Apache Webserver")
	print("2. Docker")
	print("3. Hadoop")
	print("4. Partition")
	print("5. AWS Cloud")
	print("6. LVM\n")
	text("7")

# Code for Webserver Configuration

def web():
	os.system("clear")
	text("3")
	print("1. Configure yum to get httpd software")
	print("2. Configure Apache Webserver (httpd)")
	print("3. Start httpd Services")
	print("4. Stop httpd Services")
	print("5. Permanently enable httpd Services")
	print("6. Permanently disable httpd Services\n")
	text("7")

def web_1():
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
	os.system("yum repo is Configured, now you can install or Configure httpd!")
	text("7")

def web_2():
	os.system("yum install httpd -y")
	os.system("systemctl start httpd")
	os.system("clear")
	web()
	text("2")
	os.system("Apache Webserver Configured & the httpd Service is also Started")
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
	text("6")
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
	text("6")
	print("httpd Services disabled permanently!")
	text("7")

# Code for Hadoop Configuration

def hadoop():
	os.system("clear")
	text("3")
	print("1. Configure NameNode")
	print("2. Configure DataNode")
	print("3. Start NameNode Services")
	print("4. Start DataNode Services")
	print("5. Stop NameNode Services")
	print("6. Stop DataNode Services\n")
	text("7")

def hadoop_1():
	print("Configuing NameNode")

# Code for Docker Configuration

def docker():
	os.system("clear")
	text("3")
	print("1. Configure yum repo for Docker software")
	print("2. Configure Docker & start Services")
	print("3. Start Docker Services")
	print("4. Stop Docker Services")
	print("5. Permanently enable httpd Services")
	print("6. Permanently disable httpd Services\n")
	print("7. Launch Container (OS)")
	print("8. Remove any Container")
	print("9. Add a Docker Image")
	print("10. Remove a Docker Image")
	text("7")



# Code for creating Partitions:

def partition():
	os.system("clear")
	text("3")
	print("1. Create new partition")
	print("2. Format the partition")
	print("3. Mount")
	print("4. Remove a partition")
	text("7")

# The main Code starts here:

instructions()
x = input("Enter: ")
if ("webserver" in x)
	web()
#while True:
#	os.system("clear")
#	instructions()
#	x = input("Tell me what I can do for you: ")

#	if ("webserver" in x) or ("httpd" in x):
#		web()
#		y = input("Tell me what I can do for you: ")
#		if (("configure" in y) & (("httpd" in y) or ("webserver" in y)) 