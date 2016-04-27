import boto.ec2
print "enter sg name in which u want to add and delete rules\n"
grp=raw_input()
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')
groups = conn.get_all_security_groups()
for group in groups:
	if group.id==grp :
		for rule in group.rules:
			lis=[str(integral) for integral in rule.grants]
			for i in b : 
				print i
				if rule.ip_protocol=='tcp'and i in lis:
					group.revoke(ip_protocol="tcp",cidr_ip=i)
				

	
