import boto.ec2

a=[]
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
		a.append(inst.ip_address)
b=['154.210.224.27','154.88.80.30']		

a = [str(i) for i in a]
print a 

for i in b :
	if i in a :
		print 
	else:
		print i,"Not exist"







