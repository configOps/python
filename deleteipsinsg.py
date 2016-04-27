import boto.ec2
print "enter sg name in which u want to add and delete rules\n"
grp=raw_input()
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')
groups = conn.get_all_security_groups()
b=['512.23.153.93','514.88.80.30']
for group in groups:
	if group.id==grp :
		for rule in group.rules:
			print rule
			#lis=[str(integral) for integral in rule.grants]
			#print lis
		#for i in b : 
		#	print i
		#	if rule.ip_protocol=='tcp'and i in lis:
		#		print "going to revoke"
		#		group.revoke(ip_protocol="tcp",cidr_ip=i)
		#break
				

	
