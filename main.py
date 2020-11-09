import os
import subprocess as sp
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

while True:
	os.system("clear")
	instructions()
	x = input("Tell me what I can do for you: ").lower()
	
	if (("web" in x) or ("httpd" in x) or ("1" in x)):
		web()
		y = input("Tell me what I can do for you: ").lower()

		if (("configure" in y) and (("yum" in y) or ("repo" in y)) or ("1" in y)):
			web_1()
		elif (("configure" in y) and (("httpd" in y) or ("web" in y)) or ("2" in y)):             # Apache Webserver
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
		docker()
		y = input("Tell me what I can do for you: ").lower()
		if (("configure" in y) and ("docker" in y) or ("1" in y)):
			docker_1()
		elif (("start" in y) and (("docker" in y) or ("service" in y)) or ("2" in y)):
			docker_2()
		elif (("stop" in y) and (("docker" in y) or ("service" in y)) or ("3" in y)):
			docker_3()
		elif (("enable" in y) and (("docker" in y) or ("service" in y)) or ("4" in y)):
			docker_4()
		elif (("disable" in y) and (("docker" in y) or ("service" in y)) or ("5" in y)):            # Docker Configuration
			docker_5()
		elif (("launch" in y) and (("os" in y) or ("docker" in y) or ("container" in y)) or ("6" in y)):
			docker_6()
		elif (("launch" in y) and (("web" in y) or ("httpd" in y)) and (("os" in y) or ("docker" in y) or ("container" in y)) or ("7" in y)):
			docker_7()
		elif ((("remove" in y) or ("delete" in y)) and (("os" in y) or ("docker" in y) or ("container" in y)) or ("8" in y)):
			docker_8()
		elif (("image" in y) and (("add" in y) or ("remove" in y)) or ("9" in y)):
			docker_9()
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("hadoop" in x) or ("3" in x)):
		hadoop()
		y = input("Tell me what I can do for you: ").lower()
		if (("configure" in y) and (("namenode" in y) or ("nn" in y)) or ("1" in y)):
			hadoop_1_2("namenode")
		elif (("configure" in y) and (("datanode" in y) or ("dn" in y)) or ("2" in y)):
			hadoop_1_2("datanode")
		elif (("start" in y) and (("namenode" in y) or ("nn" in y)) or ("3" in y)):                # Hadoop Configuration
			hadoop_3_4("namenode")
		elif (("start" in y) and (("datanode" in y) or ("dn" in y)) or ("4" in y)):
			hadoop_3_4("datanode")
		elif (("stop" in y) and (("namenode" in y) or ("nn" in y)) or ("5" in y)):
			hadoop_5_6("namenode")
		elif (("stop" in y) and (("datanode" in y) or ("dn" in y)) or ("6" in y)):
			hadoop_5_6("datanode")
		elif (("report" in y) or ("view" in y) or ("7" in y)):
			hadoop_7()
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("partition" in x) or ("4" in x)):
		partition()
		y = input("Tell me what I can do for you: ").lower()
		if (("block" in y) or ("harddisk" in y) or ("hd" in y) or ("storage" in y) or ("1" in y)):
			partition_1()
		elif (("detail" in y) and (("partition" in y) or ("harddisk" in y) or ("hd" in y)) or ("2" in y)):
			partition_2()
		elif (("partition" in y) and (("create" in y) or ("new" in y)) or ("3" in y)):              # Code for Partition
			partition_3()
		elif (("format" in y) or ("4" in y)):
			partition_4()
		elif (("mount" in y) or ("unmount" in y) or ("5" in y)):
			partition_5()
		elif (("partition" in y) and (("remove" in y) or ("delete" in y)) or ("6" in y)):
			partition_6()
		else:
			print("\nI can't understand you! Seems like a wrong input")
	elif (("lvm" in x) or ("logical" in x) or ("6" in x)):
		lvm()
		y = input("Tell me what I can do for you: ").lower()
		if (("view" in y) and (("volume" in y) or ("harddisk" in y) or ("hd" in y)) or ("1" in y)):
			lvm_1()
		elif (("create") and (("physical" in y) or ("pv" in y)) or ("2" in y)):
			lvm_2()
		elif ((("view" in y) or ("detail" in y)) and (("pv" in y) or ("physical" in y)) or ("3" in y)):
			lvm_3()
		elif (("create" in y) and (("group" in y) or "vg" in y) or ("4" in y)):
			lvm_4()
		elif ((("view" in y) or ("detail" in y)) and (("vg" in y) or ("group" in y)) or ("5" in y)):   # Code for LVM
			lvm_5()
		elif (("create" in y) and (("logical" in y) or "lv" in y) or ("6" in y)):
			lvm_6()
		elif ((("view" in y) or ("detail" in y)) and (("lv" in y) or ("logical" in y)) or ("7" in y)):
			lvm_7()
		elif (("extend" in y) and (("logical" in y) or ("lv" in y)) or ("8" in y)):
			lvm_8()
		elif (("extend" in y) and (("group" in y) or ("vg" in y)) or ("9" in y)):
			lvm_9()
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
print("\n\t\tThankyou! Meet you next time :)\n")
os.system("sleep 3")
os.system("clear")
text("7")