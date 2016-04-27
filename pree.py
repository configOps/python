import boto.ec2
import csv

def add_row(d):
	
    with open('document.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)
     
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

reservations = conn.get_all_instances()
#print "%s" % reservations
for res in reservations:
    for inst in res.instances:
			state="%s" %inst.state
			placement="%s" %inst.placement
			if (state=="running"):
				if 'Environment' in inst.tags:
					envtag="%s" % inst.tags['Environment']
				else:
					envtag="Nothing Mentioned"
			data=[inst.id,state,placement,envtag]
			add_row(data)

