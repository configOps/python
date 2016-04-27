import boto.ec2.autoscale


ec2_conn = boto.connect_ec2(aws_access_key_id='',aws_secret_access_key='')
as_conn = boto.connect_autoscale(aws_access_key_id='',aws_secret_access_key='')


group = as_conn.get_all_groups()
#print "no of grps"
#print group
for grp in group :
	instances_ids = [i.instance_id for i in grp.instances]
	reservations = ec2_conn.get_all_reservations(instances_ids)
	instances=[]
	for r in reservations :
		for i in r.instances:
			instances.append(i)
	for j in instances:
		data=[j.placement,j.id,j.instance_type] 
		print data
	print grp
	print len(instances)
	print "=========================================="
#reservations = conn.get_all_instances()
#print "%s" % reservations
#for grp in group: 	
