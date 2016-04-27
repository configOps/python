import boto.ec2
import csv


def add_row(d):
	
	with open('sg.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)
		
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

reservations = conn.get_all_instances()
sgarray=[]
runninginstances=[]
count=0
# go through instance list:
for i in reservations:
	for inst in i.instances:
		state="%s" %inst.state
	
		if (state=="running") :
			instcname=i.instances[0]
			runninginstances.append(instcname)
			count=count+1
print "%s" %count
for inname in runninginstances:
	
	group_nums = len(inname.groups)
	print "%s,%s" %(inname,group_nums)
	sgarray=[]		
	for z in range(group_nums):
				
		group_id = inname.groups[z].id
		sg_name = conn.get_all_security_groups(group_ids=group_id)[0]
		sgarray.append(sg_name)
	add_row(sgarray)
