import os

def text(c):
	code = "tput setaf " + c
	os.system(code)

def instructions():
	text("2")
	print("\t\tWelcome User!")
	text("3")
	print("I'm your Assistant & I can help you do these tasks:")
	print("1. Creating Partitions")
	print("2. Formatting")
	print("3. Mounting")
	print("4. Configuring Apache Webserver")
	print("5. Configuring NameNode")
	print("6. Configuring DataNode")
	print("7. Launching AWS EC2 Instance\n")
	text("7")

instructions()
x = input("Tell me what I can do: ")

def web():
	os.system("yum install httpd -y")
	os.system("systemctl start httpd")
	os.system("clear")
	instructions()
	text("2")
	print("Your httpd Web Server is Configured Successfully!")
	text("7")

if ("webserver" in x):
	web()