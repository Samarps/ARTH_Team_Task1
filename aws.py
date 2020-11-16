import os
import subprocess as sp


def text(c):
	code = "tput setaf " + c
	os.system(code)

# Code for Docker Configuration:

def aws(ssh):
	os.system("" + "clear")
	text("2")
	print("\n\t\t\t\tSub-Menu AWS operations\n")
	print("\t\t\t\t````````````````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
	text("3")
	print("1. Install & Configure AWS CLI")
	print("2. Create Key Pair & Security Group")
	print("3. Launch a new EC2 instance")
	print("4. List all instances")
	print("5. Start or Stop instance")
	print("6. Terminate instance")
	print("7. Create EBS volume")
	print("8. Attach EBS volume to instance")
	print("9. Delete EBS volume\n")
	text("7")

def aws_1(ssh):
	x = sp.getstatusoutput(ssh + "aws --version")
	if(x[0] == 0):
		os.system(ssh + "aws configure")
	else:
		os = input("Enter your OS type(e.g. Linux/Windows/Mac): ").lower()
		if(os == "linux"):
			os.system(ssh + 'curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"')
			os.system(ssh + 'unzip awscliv2.zip')
			os.system(ssh + 'sudo ./aws/install')
			os.system(ssh + "aws configure")
		elif(os == "windows"):
			os.system(ssh + 'chrome https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-windows.html')
		elif(os == "mac"):
			os.system(ssh + 'curl "https://awscli.amazonaws.com/AWSCLIV2.pkg" -o "AWSCLIV2.pkg"')
			os.system(ssh + 'sudo installer -pkg AWSCLIV2.pkg -target /')
			os.system(ssh + "aws configure")
	aws(ssh)
	print("2")
	print("\nAWS CLI done!")
	print("7")

def aws_2(ssh):
	ask = input("Enter whether to create Key pair OR Security Group: ").lower()
	if ("key" in ask):
		keyname = input("Enter unique key-pair name: ")
		os.system(ssh + "aws ec2 create-key-pair --key-name {}".format(keyname))
		aws(ssh)
		text("2")
		print("\nKey Pair created successfully")
		print("\nThe output is an ASCII version of the private key and key  fingerprint. You need to save the key to a file.")
		text("7")
	elif (("security" in ask) or ("sg" in ask)):
		sg = input("Enter security group name: ")
		os.system(ssh + "aws ec2 create-security-group --group-name {sg} --description {sg}".format(sg = sg))
		aws(ssh)
		text("2")
		print("\nSecurity Group created with name {}".format(sg))
		text("7")
	else:
		text("1")
		print("\nWrong Input!")
		text("7")

def aws_3(ssh):
	img = input("Enter image id : ")
	instype = input("Enter instance type: ")
	subnet = input("subnet id for region of instance: ")
	kn = input("Enter keyname created earlier on your account: ")
	sg = input("Enter security group name: ")
	os.system(ssh + "aws ec2 run-instances --image-id  {img}  --instance-type {instype} --subnet-id {subnet} --count 1 --key-name {kn} --security-groups {sg}".format(img = img, instype = instype, subnet = subnet, kn = kn, sg = sg))
	aws(ssh)
	text("2")
	print("\nInstance launched successfully")
	text("7")

def aws_4(ssh):
	print("Instances with detail description on your account")
	os.system(ssh + "aws ec2 describe-instances")
	aws(ssh)
	text("2")
	print("\nDetails of EC2 instances available")
	text("7")

def aws_5(ssh):
	insid = input("Enter instance id to start: ")
	os.system(ssh + "aws ec2 start-instances --instance-ids {insid}".format(insid = insid))
	aws(ssh)
	text("2")
	print("\nAWS instance started")
	text("7")

def aws_5(ssh):
	insid = input("Enter instance id to stop: ")
	os.system(ssh + "aws ec2 stop-instances --instance-ids {insid}".format(insid = insid))
	aws(ssh)
	text("2")
	print("\nAWS instance stopped")
	text("7")

def aws_6(ssh):
	insid = input("Enter instance id to terminate: ")
	os.system(ssh + "aws ec2 terminate-instances --instance-ids {insid}".format(insid = insid))
	aws(ssh)
	text("2")
	print("\nAws instance removed")
	text("7")

def aws_7(ssh):
	s = input("Size of ebs volume : ")
	region = input("Enter region where your instace available: ")
	os.system(ssh + "aws ec2 create-volume --size {s} --availability-zone {region}".format(s = s, region = region))
	aws(ssh)
	text("2")
	print("\nAws EBS volume created")
	text("7")

def aws_8(ssh):
	volid = input("Enter the volume id of your created volume: ")
	insid = input("Enter instance id to start: ")
	dev = input("Enter device name e.g. /dev/sdh or /dev/xvdh: ")
	os.system(ssh + "aws ec2 attach-volume --volume-id {volid} --instance-id {insid} --device {dev}".format(volid = volid, insid = insid, dev = dev))
	aws(ssh)
	text("2")
	print("\nAws EBS volume attached")
	text("7")

def aws_9(ssh):
	volid = input("Enter EBS volume id to delete: ")
	os.system(ssh + "aws ec2 detach-volume --volume-id {}".format(volid))
	os.system(ssh + "aws ec2 delete-volume --volume-id {}".format(volid))
	aws(ssh)
	text("2")
	print("\nAws EBS volume removed")
	text("7")