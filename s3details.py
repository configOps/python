import boto
import boto.s3.connection
import csv

def add_row(d):
	
	with open('s3details.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)
		
access_key = ''
secret_key = ''
  
        
conn = boto.s3.connect_to_region(
   region_name = 'us-east-1',
   aws_access_key_id = access_key,
   aws_secret_access_key = secret_key,
   calling_format = boto.s3.connection.OrdinaryCallingFormat()
   )
all=conn.get_all_buckets()
for bucket in all :
        #print "{name}\t\t{created}".format(name = bucket.name,created = bucket.creation_date)
        name = bucket.name
        created = bucket.creation_date.split('T')
        creation_date =created[0]
        creation_time=created[1]
        print "====================Begining of bucket============================="
        print "%s,%s,%s" %(name,creation_date,creation_time)
        data=[name,creation_date,creation_time]
        add_row(data)
        rs=bucket.list()
        data=[]
        add_row(data)
        try:
        	for key in rs:
        		name = key.name
        		size = key.size
        		modified= key.last_modified.split('T')
        		modified_date = modified[0]
        		modified_time = modified[1]
        		space=" "
        		print "%s,%s,%s,%s" %(name,size,modified_date,modified_time)
        		data=[space,name,size,modified_date,modified_time]
        		add_row(data)
        except Exception: 
  			pass
        print "========================end of bucket=============================="
        
        data=[]
        add_row(data)
print "total buckets: %s" %len(all)
               
