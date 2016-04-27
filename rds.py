import boto
import csv

rds = boto.connect_rds(aws_access_key_id='',aws_secret_access_key='')
	
def add_row(d):
	
	with open('rds.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)




instances = rds.get_all_dbinstances()
for i in instances :
	data=[i,i.instance_class,i.endpoint[0]]
	add_row(data)
