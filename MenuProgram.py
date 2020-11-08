import os

def text(c):
	code = "tput setaf " + c
	os.system(code)

def instructions():
	text("2")
	print("\n\t\t\t\t\tWelcome User!\n")
	print("\t\t\t\t\t`````````````\n")
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
	print("6. LVM")
	print("7. Exit/Close program\n")
	text("7")

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

# Code for Docker Configuration:

def docker():
	os.system("clear")
	text("2")
	print("\n\t\t\t\tSub-Menu Docker\n")
	print("\t\t\t\t```````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
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


# Code for Hadoop Configuration:

def hadoop():
	os.system("clear")
	text("2")
	print("\n\t\t\t\tSub-Menu Hadoop\n")
	print("\t\t\t\t````````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
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


# Code for creating Partitions:

def partition():
	os.system("clear")
	text("2")
	print("\n\t\t\t\tSub-Menu Partitions\n")
	print("\t\t\t\t```````````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
	text("3")
	print("1. View all the Block Devices/storage")
	print("2. View details of a HardDisk (HD) & its Partitions in detail")
	print("3. Create new partition")
	print("4. Format the partition")
	print("5. Mount & Unmount")
	print("6. Remove/delete a partition\n")
	text("7")

def partition_1():
	print("")
	os.system("lsblk")

def partition_2():
	text("6")
	print("\nYou can view HardDisk names from the 1st option, like sdb, sdc, etc")
	text("7")
	block = input("Enter the name of HardDisk: ")
	if ("sda" in block):
		block = "sda"
	elif ("sdb" in block):
		block = "sdb"
	elif ("sdc" in block):
		block = "sdb"
	else:
		print("Entered HardDisk name: {}".format(block))
	os.system("\nfdisk -l /dev/{}".format(block))

def partition_3():
	text("6")
	print("\nYou can view HardDisk names from the 1st option, they are named like sdb, sdc, etc")
	text("7")
	block = input("Enter the name of HardDisk: ").lower()
	if ("sda" in block):
		block = "sda"
	elif ("sdb" in block):
		block = "sdb"
	elif ("sdc" in block):
		block = "sdc"
	else:
		print("Entered HardDisk name: {}".format(block))
	text("6")
	print("\nRemember that you can only create either '4 Primary' OR '3 Primary + 1 Extended with multiple Logical Partitions'")
	text("7")
	ptype = input("\nEnter type of partition: Primary (p) & extended (e): ").lower()
	if ("p" in ptype):
		ptype = "p"
	elif ("e" in ptype):
		ptype = "e"
	print("Size of partition can be provided in K,M,G,T,P,etc like 2G, 1000K, 1024M, etc")
	psize = input("\nEnter size of partition: ").upper()
	os.system("rm -f new_part.sh")
	os.system("echo '#!/bin/bash' >> new_part.sh")
	os.system("echo 'fdisk /dev/{} << FDISK_CMDS' >> new_part.sh".format(block))
	os.system("echo 'n' >> new_part.sh")
	os.system("echo '{}' >> new_part.sh".format(ptype))
	os.system("echo '' >> new_part.sh")
	os.system("echo '' >> new_part.sh")
	os.system("echo '+{}' >> new_part.sh".format(psize))
	os.system("echo 'w' >> new_part.sh")
	os.system("echo 'FDISK_CMDS' >> new_part.sh")
	os.system("chmod +x new_part.sh")
	os.system("bash new_part.sh")
	os.system("udevadm settle")
	os.system("rm -f new_part.sh")
	os.system("clear")
	partition()
	text("2")
	print("\nYour new Partition is created!")
	text("7")

def partition_4():
	text("6")
	print("\nYou can view Partition name from the 1st or 2nd option, they are named like sdb1, sdb2, sdc4, etc")
	text("7")
	bpart = input("\nEnter the name of partition: ").lower()
	print("")
	os.system("mkfs.ext4 /dev/{}".format(bpart))
	os.system("clear")
	partition()
	text("2")
	print("\nYour Partition is Formatted with ext4 format!")
	text("7")

def partition_5():
	text("6")
	print("\nYou can view Partition names from the 1st option, they are named like sdb1, sdb2, sdc4, etc")
	text("7")
	bpart = input("\nEnter the name of partition: ").lower()
	mount = input("Enter 1 for mount & 2 for unmount: ")
	if mount == "1":
		mfold = input("\nEnter complete path of folder/directory to mount: ")
		os.system("mkdir {}".format(mfold))
		os.system("mount /dev/{} {}".format(bpart, mfold))
		os.system("clear")
		partition()
		text("2")
		print("\nMounted Successfully!")
		text("7")
	elif mount == "2":
		mfold = input("\nEnter complete path of folder/directory to mount: ")
		os.system("umount {}".format(mfold))
		os.system("clear")
		partition()
		text("2")
		print("\nUnmounted Successfully!")
		text("7")
	else:
		partition()
		text("1")
		print("Wrong Input!")
		text("7")

def partition_6():
	text("6")
	print("\nYou can view HardDisk (HD) & Partition name from the 1st or 2nd option, HD are named like sdb, sdc, etc")
	print("Partitions are named like sdb1, sdb2, sdc4, etc")
	text("7")
	block = input("\nEnter HardDisk name: ").lower()
	bpart = input("\nEnter the name of partition: ").lower()
	print("")
	z = 1
	while z<10:
		if (str(z) in bpart):
			break
		z += 1
	os.system("rm -f rem_part.sh")
	os.system("echo '#!/bin/bash' >> rem_part.sh")
	os.system("echo 'fdisk /dev/{} << FDISK_CMDS' >> rem_part.sh".format(block))
	os.system("echo 'd' >> rem_part.sh")
	os.system("echo '{}' >> rem_part.sh".format(z))
	os.system("echo 'w' >> rem_part.sh")
	os.system("echo 'FDISK_CMDS' >> rem_part.sh")
	os.system("chmod +x rem_part.sh")
	os.system("bash rem_part.sh")
	os.system("rm -f rem_part.sh")
	os.system("clear")
	partition()
	text("2")
	print("\nPartition deleted!")
	text("7")


# The main Code starts here:

while True:
	os.system("clear")
	instructions()
	x = input("Tell me what I can do for you: ").lower()
	
	if (("web" in x) or ("httpd" in x) or ("1" in x)):
		web()
		y = input("Tell me what I can do for you: ").lower()

		if (("configure" in y) and (("yum" in y) or ("repo" in y)) or ("1" in y)):
			web_1()
		elif (("configure" in y) and (("httpd" in y) or ("web" in y)) or ("2" in y)):
			web_2()
		elif (("start" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("3" in y)):
			web_3()
		elif (("stop" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("4" in y)):
			web_4()
		elif (("enable" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("5" in y)):
			web_5()
		elif (("disable" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("3" in y)):
			web_6()
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("docker" in x) or ("2" in x)):
		y = input("Tell me what I can do for you: ").lower()
	elif (("partition" in x) or ("4" in x)):
		partition()
		y = input("Tell me what I can do for you: ").lower()
		if (("block" in y) or ("harddisk" in y) or ("storage" in y) or ("1" in y)):
			partition_1()
		elif (("detail" in y) and (("partition" in y) or ("harddisk" in y) or ("hd" in y)) or ("2" in y)):
			partition_2()
		elif (("partition" in y) and (("create" in y) or ("new" in y)) or ("3" in y)):
			partition_3()
		elif (("format" in y) or ("4" in y)):
			partition_4()
		elif (("mount" in y) or ("unmount" in y) or ("5" in y)):
			partition_5()
		elif (("partition" in y) and (("remove" in y) or ("delete" in y)) or ("6" in y)):
			partition_6()
	elif (("7" in x) or ("exit" in x) or ("close" in x)):
		break
	else:
		print("\nI can't understand you! Please try again")

	text("6")
	input("\nPress ENTER to Continue...")
	text("7")


text("2")
print("\n\t\tThankyou! Meet you next time :)\n")
os.system("sleep 3")
os.system("clear")
text("7")