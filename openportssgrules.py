import boto.ec2
import csv
def add_row(d):
	
    with open('1.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)

conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

groups = conn.get_all_security_groups()

count=0
for z in groups:
	port=[]
	
	rule_nums = len(z.rules)
	#print "----------------------------------------------------------------------------------------------------------"
	
	count =0
	for g in range(rule_nums):
		#print type(z.rules[g].grants[0])
		source = [str(integral) for integral in z.rules[g].grants]
		#print type(source[0])
		
		if '0.0.0.0/0' in source :
			print  ' %s===%s' %(z , z.rules[g])
			count=count+1
	#print count
	#if count >0 :
	#	print "%s // %s" %(z,count)
			
				
