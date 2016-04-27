import boto.ec2
import csv
def add_row(d):
	
    with open('inbound3.0.csv', 'a') as f:
		a = csv.writer(f, delimiter=',')
		a.writerow(d)

    
conn=boto.ec2.connect_to_region("us-east-1", aws_access_key_id='',aws_secret_access_key='')

groups = conn.get_all_security_groups()


for z in groups:
	ingress=[]
	
	rule_nums = len(z.rules)
	#print "----------------------------------------------------------------------------------------------------------"
	print "%s grp name" %z
	for g in range(rule_nums):
		ingress.append("Port/protocol: %s  Source: %s" % (z.rules[g],z.rules[g].grants))
	add_row(ingress)
			
				

#for z in groups:
#	egress=[]
	
#	print "%s grp name" %z
#	rule_nums = len(z.rules_egress)
	#print "%s" %rule_nums
	#print "----------------------------------------------------------------------------------------------------------"
#	print "%s" %z
#	for g in range(rule_nums):
		#print z.rules_egress[g]
		#print #
#		egress.append("Port/protocol: %s  Destination: %s" % (z.rules_egress[g],z.rules_egress[g].grants))
#		add_row(egress)
	#break
