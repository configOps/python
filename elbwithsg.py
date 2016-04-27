import boto.ec2.elb

conn = boto.ec2.elb.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

lblist=conn.get_all_load_balancers()

for i in lblist :
	print i.name , i.security_groups
