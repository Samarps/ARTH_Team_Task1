import os
import subprocess as sp
import getpass
import web
from web import *
import docker
from docker import *
import hadoop
from hadoop import *
import partition
from partition import *
import lvm
from lvm import *
import aws
from aws import *

ssh = ""

def text(c):
	code = "tput setaf " + c
	os.system(code)

def intro():
	os.system("" + "clear")
	print("\n\t\t\t\t\t ARTH2020.9.12")
	print("\t\t\t\t\t_______________\n")
	text("2")
	print("\n\t\t\t\t\tWelcome User!\n")
	print("\t\t\t\t\t`````````````\n")
	text("6")
	print("\n\t\t\t\bThis program will help you configure Operating systems!")
	print("\t\t\bI can Configure OS locally (base OS) or any remote OS through SSH protocol\n")
	text("3")
	print("\n\t\t\t\bENTER WHICH SYSTEM YOU NEED TO CONFIGURE (local/remote)\n")
	text("7")

def remote_ip(z_ip):
	if z_ip != "":
		r_ip = z_ip
	else:
		r_ip = ""
	return r_ip

def config_os():
	choice = input("\t\t\t\t\t: ")
	if choice == "remote":
		remote_ip = input("\n\n\n\tEnter IP Address of the remote system: ")
		remote_ip(remote_ip)
		rpass = getpass.getpass("\n\tEnter password: ")
		ssh = "sshpass -p {} ssh root@{} ".format(rpass, z_ip)
		text("2")
		print("\n\n\n\n\t\t\t\t\b\b\bProceeding with Remote System Configuration!")
		text("7")
		os.system("" + "sleep 2.5")
		os.system("" + "clear")
	else:
		ssh = ""
		text("2")
		print("\n\n\n\n\t\t\t\t\b\b\bProceeding with Local System Configuration!")
		text("7")
		os.system("" + "sleep 2.5")
		os.system("" + "clear")
	return ssh

intro()
ssh = config_os()
z_ip = ""
r_ip = remote_ip(z_ip)


def instructions(ssh):
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

while True:
	os.system("" + "clear")
	instructions(ssh)
	x = input("Tell me what I can do for you: ").lower()
	
	if (("web" in x) or ("httpd" in x) or ("1" in x)):
		web(ssh)
		y = input("Tell me what I can do for you: ").lower()

		if (("configure" in y) and (("yum" in y) or ("repo" in y)) or ("1" in y)):
			web_1(ssh, r_ip)
		elif (("configure" in y) and (("httpd" in y) or ("web" in y)) or ("2" in y)):             # Apache Webserver
			web_2(ssh)
		elif (("start" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("3" in y)):
			web_3(ssh)
		elif (("stop" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("4" in y)):
			web_4(ssh)
		elif (("enable" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("5" in y)):
			web_5(ssh)
		elif (("disable" in y) and (("httpd" in y) or ("web" in y) or ("service" in y)) or ("6" in y)):
			web_6(ssh)
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("docker" in x) or ("2" in x)):
		docker(ssh)
		y = input("Tell me what I can do for you: ").lower()
		if (("configure" in y) and ("docker" in y) or ("1" in y)):
			docker_1(ssh, r_ip)
		elif (("start" in y) and (("docker" in y) or ("service" in y)) or ("2" in y)):
			docker_2(ssh)
		elif (("stop" in y) and (("docker" in y) or ("service" in y)) or ("3" in y)):
			docker_3(ssh)
		elif (("enable" in y) and (("docker" in y) or ("service" in y)) or ("4" in y)):
			docker_4(ssh)
		elif (("disable" in y) and (("docker" in y) or ("service" in y)) or ("5" in y)):            # Docker Configuration
			docker_5(ssh)
		elif (("launch" in y) and (("os" in y) or ("docker" in y) or ("container" in y)) or ("6" in y)):
			docker_6(ssh)
		elif (("launch" in y) and (("web" in y) or ("httpd" in y)) and (("os" in y) or ("docker" in y) or ("container" in y)) or ("7" in y)):
			docker_7(ssh)
		elif ((("remove" in y) or ("delete" in y)) and (("os" in y) or ("docker" in y) or ("container" in y)) or ("8" in y)):
			docker_8(ssh)
		elif (("image" in y) and (("add" in y) or ("remove" in y)) or ("9" in y)):
			docker_9(ssh)
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("hadoop" in x) or ("3" in x)):
		hadoop(ssh)
		y = input("Tell me what I can do for you: ").lower()
		if (("configure" in y) and (("namenode" in y) or ("nn" in y)) or ("1" in y)):
			hadoop_1_2(ssh, "namenode", r_ip)
		elif (("configure" in y) and (("datanode" in y) or ("dn" in y)) or ("2" in y)):
			hadoop_1_2(ssh, "datanode", r_ip)
		elif (("start" in y) and (("namenode" in y) or ("nn" in y)) or ("3" in y)):                # Hadoop Configuration
			hadoop_3_4(ssh, "namenode")
		elif (("start" in y) and (("datanode" in y) or ("dn" in y)) or ("4" in y)):
			hadoop_3_4(ssh, "datanode")
		elif (("stop" in y) and (("namenode" in y) or ("nn" in y)) or ("5" in y)):
			hadoop_5_6(ssh, "namenode")
		elif (("stop" in y) and (("datanode" in y) or ("dn" in y)) or ("6" in y)):
			hadoop_5_6(ssh, "datanode")
		elif (("report" in y) or ("view" in y) or ("7" in y)):
			hadoop_7(ssh)
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("partition" in x) or ("4" in x)):
		partition(ssh)
		y = input("Tell me what I can do for you: ").lower()
		if (("block" in y) or ("harddisk" in y) or ("hd" in y) or ("storage" in y) or ("1" in y)):
			partition_1(ssh)
		elif (("detail" in y) and (("partition" in y) or ("harddisk" in y) or ("hd" in y)) or ("2" in y)):
			partition_2(ssh)
		elif (("partition" in y) and (("create" in y) or ("new" in y)) or ("3" in y)):              # Code for Partition
			partition_3(ssh)
		elif (("format" in y) or ("4" in y)):
			partition_4(ssh)
		elif (("mount" in y) or ("unmount" in y) or ("5" in y)):
			partition_5(ssh)
		elif (("partition" in y) and (("remove" in y) or ("delete" in y)) or ("6" in y)):
			partition_6(ssh)
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("aws" in x) or ("5" in x)):
		aws(ssh)
		y = input("Tell me what I can do for you: ").lower()
		if (("install" in y) or ("config" in y) or ("1" in y)):
			aws_1(ssh)
		elif (("key" in y) or ("security" in y) or ("sg" in y) or ("2" in y)):
			aws_2(ssh)
		elif ((("launch" in y) or ("new" in y)) and (("instance" in y) or ("ec2" in y)) or ("3" in y)):
			aws_3(ssh)
		elif (("list" in y) and ("instance" in y) or ("4" in y)):
			aws_4(ssh)
		elif (("instance" in y) and (("stop" in y) or ("start" in y)) or ("5" in y)):                 # Code for AWS
			aws_5(ssh)
		elif (("instance" in y) and ("terminate" in y) or ("6" in y)):
			aws_6(ssh)
		elif (("create" in y) and (("volume" in y) or ("ebs" in y)) or ("7" in y)):
			aws_7(ssh)
		elif (("attach" in y) and (("volume" in y) or ("ebs" in y)) or ("8" in y)):
			aws_8(ssh)
		elif ((("delete" in y) or ("remove" in y)) and (("volume" in y) or ("ebs" in y)) or ("9" in y)):
			aws_9(ssh)
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("lvm" in x) or ("logical" in x) or ("6" in x)):
		lvm(ssh)
		y = input("Tell me what I can do for you: ").lower()
		if (("view" in y) and (("volume" in y) or ("harddisk" in y) or ("hd" in y)) or ("1" in y)):
			lvm_1(ssh)
		elif (("create") and (("physical" in y) or ("pv" in y)) or ("2" in y)):
			lvm_2(ssh)
		elif ((("view" in y) or ("detail" in y)) and (("pv" in y) or ("physical" in y)) or ("3" in y)):
			lvm_3(ssh)
		elif (("create" in y) and (("group" in y) or "vg" in y) or ("4" in y)):
			lvm_4(ssh)
		elif ((("view" in y) or ("detail" in y)) and (("vg" in y) or ("group" in y)) or ("5" in y)):   # Code for LVM
			lvm_5(ssh)
		elif (("create" in y) and (("logical" in y) or "lv" in y) or ("6" in y)):
			lvm_6(ssh)
		elif ((("view" in y) or ("detail" in y)) and (("lv" in y) or ("logical" in y)) or ("7" in y)):
			lvm_7(ssh)
		elif (("extend" in y) and (("logical" in y) or ("lv" in y)) or ("8" in y)):
			lvm_8(ssh)
		elif (("extend" in y) and (("group" in y) or ("vg" in y)) or ("9" in y)):
			lvm_9(ssh)
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("7" in x) or ("exit" in x) or ("close" in x)):                                           # Exit/Close Program
		break
	else:
		print("\nI can't understand you! Please try again")                                         # Wrong Input!

	text("6")
	input("\nPress ENTER to Continue...")
	text("7")


text("2")
print("\n\n\n\t\t\t\tThankyou! Meet you next time :)\n")
os.system(ssh + "sleep 3")
os.system("" + "clear")
text("7")