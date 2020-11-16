import os
import subprocess as sp


def text(c):
	code = "tput setaf " + c
	os.system(code)

# Code for Docker Configuration:

def docker(ssh):
	os.system("" + "clear")
	text("2")
	print("\n\t\t\t\tSub-Menu Docker\n")
	print("\t\t\t\t```````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
	text("3")
	print("1. Configure Docker & start Services")
	print("2. Start Docker Services")
	print("3. Stop Docker Services")
	print("4. Permanently enable Docker Services")
	print("5. Permanently disable Docker Services")
	print("6. Launch Container/Docker (OS)")
	print("7. Launch Docker with Webserver Configured (& webpages hosted)")
	print("8. Remove any Container/Docker OS")
	print("9. Add/remove any Docker Image\n")
	text("7")

def docker_1(ssh):
	os.system(ssh + "rm -f /etc/yum.repos.d/docker-ce.repo")
	os.system(ssh + "sudo dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo")
	os.system(ssh + "sudo dnf install --nobest docker-ce -y")
	os.system(ssh + "systemctl start docker")
	docker(ssh)
	text("2")
	print("Docker stable version Installed & Service is also Started")
	text("7")

def docker_2(ssh):
	os.system(ssh + "systemctl start docker")
	docker(ssh)
	text("2")
	print("docker Services started!")
	text("7")

def docker_3(ssh):
	os.system(ssh + "systemctl stop docker")
	docker(ssh)
	text("2")
	print("docker Services stopped!")
	text("7")

def docker_4(ssh):
	os.system(ssh + "systemctl enable docker")
	docker(ssh)
	text("2")
	print("docker Services enabled permanently!")
	text("7")

def docker_5(ssh):
	os.system(ssh + "systemctl disable docker")
	docker(ssh)
	text("2")
	print("docker Services disabled permanently!")
	text("7")

def docker_6(ssh):
	name = input("Enter your docker name: ")
	osname = input("Enter Operating System (OS) name")
	out = sp.getstatusoutput(ssh + "docker run -dit --name {name} {osname}".format(name=name,osname=osname))
	docker(ssh)
	text("2")
	print("Docker launched with ID")
	text("7")
	print(out[1])

def docker_7(ssh):
	name = input("Enter name of OS: ")
	srcfile = input("Enter Source code location in your host OS: ")
	port = input("Enter proxy port inside Docker: ")
	t = sp.getstatusoutput(ssh + "docker run -dit --name {name} -p {port}:80 -v {src}:/usr/local/apache2/htdocs/   httpd:2.4".format(name=name,src=srcfile,port=port))
	docker(ssh)
	text("2")
	print("\nDocker successfully launched with ID")
	text("7")
	print(t[1])

def docker_8(ssh):
	sp.getstatusoutput(ssh + "docker ps -a")
	dockerid = input("Enter id upto 5 place from left")
	os.system(ssh + "docker rm {did}".format(did=dockerid))
	docker(ssh)
	text("2")
	print("\nDocker OS removed Successfully!")
	text("7")

def docker_9(ssh):
	ask = input("If you want to add/pull image enter 'a', otherwise to remove enter 'r': ").lower()
	if ask == 'a':
		image = input("Enter image name to add to local: ")
		add = sp.getstatusoutput(ssh + "docker pull {image}".format(image=image))
		print(add[1])
		docker(ssh)
		text("2")
		print("\nDocker image added/pulled Successfully!")
		text("7")
	elif ask == 'r':
		os.system(ssh + "docker images")
		image = input("Enter image name to remove : ")
		os.system(ssh + "docker rmi {image}".format(image=image))
		docker(ssh)
		text("2")
		print("\nDocker image removed Successfully!")
		text("7")
	else:
		text("1")
		print("\nWrong input!")
		text("7")
