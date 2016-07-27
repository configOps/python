
import boto3


my_inputs=[]
print "\n Please enter Instance id and ami name to create and update ami in Autoscaling group \n "
my_inputs.append(raw_input())
my_inputs.append(raw_input())
instid=my_inputs[0]
aminame=my_inputs[1]
print "\n Pls enter autoscaling group which you want to update and enter the name of new launch config which u want to associate with this autoscaling group \n"
my_inputs.append(raw_input())
my_inputs.append(raw_input())
ag_to_copy=my_inputs[2]
lc_name=my_inputs[3]
#print instid ,"instance id from which image is going to create"
print "###################################################################################"
print "Ami will be created with instance id ",instid,"and ami name",aminame
print "###################################################################################"

def createimg(instid,aminame):
	client1 = boto3.client('ec2')
	response=client1.create_image(InstanceId=instid, Name=aminame,NoReboot=True)
	my_inputs.append(response['ImageId'])
	return;

createimg(instid,aminame);
img_id=my_inputs[4]
print "###################################################################"
print "Ami is created with id ",img_id
print "###################################################################"
'''
img_id=res['LaunchConfigurations'][0]['ImageId']
'''


def copyLC(img_id,ag_to_copy,lc_name) :
	client = boto3.client('autoscaling')
	rep=client.describe_auto_scaling_groups(AutoScalingGroupNames=[
        ag_to_copy])
	my_inputs.append(rep['AutoScalingGroups'][0]['LaunchConfigurationName'])
	lc_to_copy=my_inputs[5]
	#print lc_to_copy , "lc to copy"
	print "Copying Launch Configuration",lc_to_copy,"to",lc_name,".............."
	res = client.describe_launch_configurations(LaunchConfigurationNames=[lc_to_copy],)
	user_data = res['LaunchConfigurations'][0]['UserData']
	key = res['LaunchConfigurations'][0]['KeyName']
	sg = res['LaunchConfigurations'][0]['SecurityGroups']
	ins_type = res['LaunchConfigurations'][0]['InstanceType']
#vpc_id = res['LaunchConfigurations'][0]['ClassicLinkVPCId']
	vpc_sg = res['LaunchConfigurations'][0]['ClassicLinkVPCSecurityGroups']
	kid = res['LaunchConfigurations'][0]['KernelId']
	rid = res['LaunchConfigurations'][0]['RamdiskId']
	monitoring = res['LaunchConfigurations'][0]['InstanceMonitoring']
#pubip = res['LaunchConfigurations'][0]['AssociatePublicIpAddress']
	ebsopt = res['LaunchConfigurations'][0]['EbsOptimized']
	bdm = res['LaunchConfigurations'][0]['BlockDeviceMappings']
	print "Creating launch configuration",lc_name,"............................."
	req = client.create_launch_configuration(
LaunchConfigurationName=lc_name,
ImageId=img_id,
KeyName=key,
SecurityGroups=sg,
	 #   ClassicLinkVPCId='string',
    	ClassicLinkVPCSecurityGroups=vpc_sg,
    	UserData=user_data,
   # InstanceId='string',
    InstanceType=ins_type,
   # KernelId=kid,
    #RamdiskId=rid,
    BlockDeviceMappings=bdm,
    InstanceMonitoring=monitoring,
   # SpotPrice='string',
  #  IamInstanceProfile='string',
    EbsOptimized=ebsopt
  #  AssociatePublicIpAddress=True|False,
   # PlacementTenancy='string'
)

copyLC(img_id,ag_to_copy,lc_name);



def changeLcinAg(lc_name,ag_to_copy):
	print "Updating Launch Conifguration",lc_name,"in Autoscaling group",ag_to_copy
	client4 = boto3.client('autoscaling')
	response4 = client4.update_auto_scaling_group(AutoScalingGroupName=ag_to_copy,LaunchConfigurationName=lc_name)
	print "Modified Autoscaling grp to have launch configuration as",lc_name
	return;

changeLcinAg(lc_name,ag_to_copy);
	



