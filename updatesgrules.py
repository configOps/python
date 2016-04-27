import boto.ec2
print "enter sg name in which u want to add and delete rules\n"
grp=raw_input()

#3.0       
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')#enter ur credentials
#2.0 
#conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')


#find list of sg where ssh 22 is open for 0.0.0.0/0

'''sg=[]
groups = conn.get_all_security_groups()
count=0
for group in groups:
	if group.id==grp :
    	print group.id
    	for rule in group.rules:
    		lis=[str(integral) for integral in rule.grants]
    		if rule.ip_protocol=='tcp'and rule.from_port=='22'and rule.to_port=='22'and '0.0.0.0/0' in lis:
    			print group.name,group.id
    			count=count+1
	print count
	return sg '''
	
	
# Add rule for contractor ips and remove ssh 22 for 0.0.0.0/0  I tried script with "testupdatewithboto" sg.

groups = conn.get_all_security_groups()
for group in groups:
	if group.id==grp :
		for rule in group.rules:
			lis=[str(integral) for integral in rule.grants]
			if rule.ip_protocol=='tcp'and rule.from_port=='22'and rule.to_port=='22'and '0.0.0.0/0' in lis:
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="1")
				group.authorize(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="3")
				
				group.revoke(ip_protocol="tcp", from_port=22, to_port=22, cidr_ip="0.0.0.0/0")
				

	
