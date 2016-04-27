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
	state="%s" %inst.state
	state=state.encode('utf-8')
	if state =='running':
		if 'Name' in inst.tags:
			name="%s" %inst.tags['Name']
		else :
			name='Nothing Mentioned'
		if 'Environment' in inst.tags:
			envtag="%s" % inst.tags['Environment']
		else:
			envtag="Nothing Mentioned"
		instid="%s" % inst.id
		data=[name,instid,envtag,state]
		add_row(data)
