import sys
import boto
import pprint

del_flag = ''
if len(sys.argv) > 1:
    del_flag = sys.argv[1]

pp = pprint.PrettyPrinter(indent=4)

ACCESS_KEY=""
SECRET_KEY=""
ec2 = boto.connect_ec2(ACCESS_KEY, SECRET_KEY)

allgroups = []

groups = ec2.get_all_security_groups()
for groupobj in groups:
    allgroups.append(groupobj.name)

groups_in_use = []
for state in ['running','stopped']:
    allinstances = ec2.get_all_instances(filters={'instance-state-name': state})
    for r in allinstances:
        for inst in r.instances:
            if inst.groups[0].name not in groups_in_use:
                groups_in_use.append(inst.groups[0].name)

delete_candidates = []
for group in allgroups:
    if group not in groups_in_use:
        delete_candidates.append(group)

#if del_flag == '--delete':
#    print "identified to not be in use."
#   for group in delete_candidates:
#        ec2.delete_security_group(group)
#   print "We have deleted %d groups." % (len(delete_candidates))
#else:
print "groups to be removed "
    #print "Run this again with `--delete` to remove them"
pp.pprint(sorted(delete_candidates))
print "Total of %d groups for removal." % (len(delete_candidates))
