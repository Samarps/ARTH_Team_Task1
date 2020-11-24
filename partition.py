import os
import subprocess as sp


def text(c):
	code = "tput setaf " + c
	os.system(code)

# Code for creating Partitions:

def partition(ssh):
	os.system("" + "clear")
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

def partition_1(ssh):
	print("")
	os.system(ssh + "lsblk")

def partition_2(ssh):
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
	print("")
	os.system(ssh + "fdisk -l /dev/{}".format(block))

def partition_3(ssh, r_ip):
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
	os.system(ssh + "rm -f new_part.sh")
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
	os.system(ssh + "scp new_part.sh {}:/root/".format(r_ip))
	os.system(ssh + "udevadm settle")
	os.system(ssh + "rm -f new_part.sh")
	partition(ssh)
	text("2")
	print("\nYour new Partition is created!")
	text("7")

def partition_4(ssh):
	text("6")
	print("\nYou can view Partition name from the 1st or 2nd option, they are named like sdb1, sdb2, sdc4, etc")
	text("7")
	bpart = input("\nEnter the name of partition: ").lower()
	print("")
	os.system(ssh + "mkfs.ext4 /dev/{}".format(bpart))
	partition(ssh)
	text("2")
	print("\nYour Partition is Formatted with ext4 format!")
	text("7")

def partition_5(ssh):
	text("6")
	print("\nYou can view Partition names from the 1st option, they are named like sdb1, sdb2, sdc4, etc")
	text("7")
	bpart = input("\nEnter the name of partition: ").lower()
	mount = input("You want to mount (m) OR unmount (u): ")
	if (("m" in mount) or ("mount" in mount)):
		mfold = input("\nEnter complete path of folder/directory to mount: ")
		os.system(ssh + "mkdir {}".format(mfold))
		os.system(ssh + "mount /dev/{} {}".format(bpart, mfold))
		partition(ssh)
		text("2")
		print("\nMounted Successfully!")
		text("7")
	elif (("u" in mount) or ("unmount" in mount)):
		mfold = input("\nEnter complete path of folder/directory to mount: ")
		os.system(ssh + "umount {}".format(mfold))
		partition(ssh)
		text("2")
		print("\nUnmounted Successfully!")
		text("7")
	else:
		partition(ssh)
		text("1")
		print("Wrong Input!")
		text("7")

def partition_6(ssh, r_ip):
	text("6")
	print("\nYou can view HardDisk (HD) & Partition name from the 1st or 2nd option, HD are named like sdb, sdc, etc")
	print("Partitions are named like sdb1, sdb2, sdc4, etc")
	text("7")
	block = input("\nEnter HardDisk name: ").lower()
	bpart = input("\nEnter the name of partition: ").lower()
	print("\n")
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
	partition(ssh)
	text("2")
	print("\nPartition deleted!")
	text("7")
