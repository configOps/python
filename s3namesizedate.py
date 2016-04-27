import boto
import boto.s3.connection
import csv

def add_row(d):
	
	with open('s3sizenname2.0.csv', 'a') as f:
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
#all=conn.get_all_buckets()
#for bucket in all :
        #print "{name}\t\t{created}".format(name = bucket.name,created = bucket.creation_date)
size=0
        #name = bucket.name
        #created = bucket.creation_date.split('T')
        #creation_date =created[0]
        #creation_time=created[1]
#bucket='grindr-fluentd'
bucket = conn.get_bucket('grindr-fluentd') 
       # try:
number_of_keys = len(bucket.get_all_keys())
for key in bucket.list():
	size += key.size
        #except Exception: 
  		#	pass
print size
print bucket.name
print number_of_keys
        #print "%s,%s,%s" %(bucket.name,size)
        #data=[name,creation_date,creation_time]
        #add_row(data)
#print "total buckets: %s" %len(all)
