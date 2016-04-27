from boto import rds
import csv

def add_row(d):
	
    with open('document.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = 'Y'

# connect
rds_conn = rds.RDSConnection(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

# list all db instances
dbinstances = rds_conn.get_all_dbinstances()
for dbi in dbinstances:
	#print dbi,dbi.endpoint,dbi.instance_class
	name=dbi
	end=dbi.endpoint[0]
	sizes=dbi.instance_class
	print name,end,sizes
    #data=[name,end,sizes]
    #add_row(data)
    
