import boto
s3 = boto.connect_s3('', '')

def get_bucket_size(bucket_name):
    bucket = s3.lookup(bucket_name)
    total_bytes = 0
    n = 0
    for key in bucket:
        total_bytes += key.size
        n += 1
        if n % 2000 == 0:
            print n
    total_gigs = total_bytes/1024/1024/1024
    print "%s: %i GB, %i objects" % (bucket_name, total_gigs, n)
    return total_gigs, n

bucket_list = []
bucket_sizes = []



for bucket_name in bucket_list:
    size, object_count = get_bucket_size(bucket_name)
    bucket_sizes.append(dict(name=bucket_name, size=size, count=object_count))

print "\nTotals:"
for bucket_size in bucket_sizes:
    print "%s: %iGB, %i objects" % (bucket_size["name"], bucket_size["size"], bucket_size["count"])
