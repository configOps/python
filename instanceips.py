
import boto.ec2
import sys

def txt(content):
	
	with open("Output.txt", "a") as text_file:
		text_file.write("%s\n" % content)

conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',
aws_secret_access_key='')
reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
		print inst.ip_address
		if inst.ip_address!=None:
			txt(inst.ip_address)







