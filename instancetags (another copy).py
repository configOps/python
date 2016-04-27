import boto.ec2
import csv

def add_row(d):
	
    with open('document.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)
#3.0       
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

reservations = conn.get_all_instances()
#print "%s" % reservations
for res in reservations:
    for inst in res.instances:
		if 'Name' in inst.tags:
			state="%s" %inst.state
			if state=="running":
				if 'Environment' not in inst.tags: 
					instid="%s" % inst.id
					envtag="Nothing Mentioned"
					name="%s" %inst.tags['Name']
					data=[name,instid,envtag,state]
					add_row(data)
	



