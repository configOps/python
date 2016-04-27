import boto.dynamodb
#import boto3
import csv

conn = boto.dynamodb.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')
def add_row(d):
	
	with open('dynamonew.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)

instances=conn.list_tables()
#client = boto3.client('dynamodb'))
for i in instances:
	table=conn.get_table(i)
	data=[table.name,table.read_units,table.write_units,table.schema.hash_key_name,table.schema.range_key_name,conn.describe_table(table.name)['Table']['TableSizeBytes']]
	add_row(data)
	#print conn.describe_table(table.name)
