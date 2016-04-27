import boto.dynamodb
from boto.dynamodb2.table import Table
conn = boto.dynamodb.connect_to_region(
        'us-west-2',
        aws_access_key_id='',
        aws_secret_access_key='')
print conn
print conn.list_tables()
table2= conn.get_table('table1')
result=table2.query( hash_key="44720449")
for i in result:
	print i["Timestamp"] 
###
#specific_rows=table2.scan(Timestamp_eq="1421568582501596")
#for r in specific_rows:
#	print r['MessageId']
###
