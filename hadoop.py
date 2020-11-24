import os
import subprocess as sp


def text(c):
	code = "tput setaf " + c
	os.system(code)

# Code for Hadoop Configuration:

def hadoop(ssh):
	os.system("" + "clear")
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
	print("6. Stop DataNode Services")
	print("7. View report of the Hadoop Cluster\n")
	text("7")

def hdfs_file(ssh, r_ip):
	os.system("echo '<?xml version=\"1.0\"?>' >> hdfs-site.xml")
	os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n' >> hdfs-site.xml")
	os.system("echo '<!-- Put site-specific property overrides in this file. -->\n' >> hdfs-site.xml")
	os.system("echo '<configuration>\n<property>\n<name>dfs.name.dir</name>' >> hdfs-site.xml")
	os.system("echo '<value>/nn</value>\n</property>\n</configuration>' >> hdfs-site.xml")
	if ssh != "":
		os.system("scp hdfs-site.xml {}:/root/".format(r_ip))
	os.system(ssh + "mv -f hdfs_file.xml /etc/hadoop/")

def core_file(ssh, ip, r_ip):
	os.system("echo '<?xml version=\"1.0\"?>' >> core-site.xml")
	os.system("echo '<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n' >> core-site.xml")
	os.system("echo '<!-- Put site-specific property overrides in this file. -->\n' >> core-site.xml")
	os.system("echo '<configuration>\n<property>\n<name>fs.default.name</name>' >> core-site.xml")
	os.system("echo '<value>hdfs://{}:9001</value>\n</property>\n</configuration>' >> core-site.xml".format(ip))
	if ssh != "":
		os.system("scp core-site.xml {}:/root/".format(r_ip))
	os.system(ssh + "mv -f core_file.xml /etc/hadoop/")

def hadoop_1_2(ssh, node, r_ip):
	if node == "namenode":
		ip = "0.0.0.0"
	elif node == "datanode":
		ip = input("Enter the IP Address of the NameNode: ")
	text("2")
	print("\nWait it may take few minutes, we're downloading & installing some softwares\n")
	text("7")
	os.system(ssh + "sleep 2")
	os.system(ssh + "pip3 install gdown")
	os.system(ssh + "gdown --id 1ilqY9Yj-doBCO4jktWD2rOuYpKHLIti5")     # downloading java & hadoop softwares
	os.system(ssh + "gdown --id 1LkQ5J_EnfC1P0jelIvkmslraHhwKnN_m")
	os.system(ssh + "rpm -ivh jdk-8u171-linux-x64.rpm")
	os.system("rm -rf my.sh")
	os.system("echo '#!/bin/bash' > my.sh")
	os.system("echo 'echo 3 > /proc/sys/vm/drop_caches' >> my.sh")
	os.system("chmod +x my.sh")
	os.system(ssh + "scp my.sh {}:/root/".format(r_ip))
	os.system(ssh + "bash my.sh")
	os.system(ssh + "rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force")         # installing the softwares
	hdfs_file(ssh, r_ip)
	core_file(ssh, ip, r_ip)
	if node == "namenode":
		os.system(ssh + "hadoop namenode -format")
	os.system(ssh + "bash my.sh")
	os.system(ssh + "hadoop-daemon.sh start {}".format(node))
	os.system(ssh + "rm -rf my.sh")
	hadoop(ssh)
	text("2")
	print("\nYour {} is Configured Successfully & service also Started!".format(node))
	text("7")

def hadoop_3_4(ssh, node):
	os.system(ssh + "hadoop-daemon.sh start {}".format(node))
	hadoop(ssh)
	text("2")
	print("\nYour {} Service Started!".format(node))
	text("7")

def hadoop_5_6(ssh, node):
	os.system(ssh + "hadoop-daemon.sh stop {}".format(node))
	hadoop(ssh)
	text("2")
	print("\nYour {} Service Started!".format(node))
	text("7")

def hadoop_7(ssh):
	print("")
	os.system(ssh + "hadoop dfsadmin -report")
