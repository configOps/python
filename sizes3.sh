#!/bin/sh
buckets=`s3cmd -c /Users/preetisharma/.s3cfg ls | awk '{FS=" ";print $3}'`
#for bucket in $buckets
#do
#size=`s3cmd -c /Users/preetisharma/.s3cfg du "$bucket" |awk '{FS=" ";print $1}'`
#sizemb=`expr $size / \\( 1024 \\* 1024 \\)`
#sizegb=`expr $sizemb / 1024`
#echo "$bucket ${sizegb} GB ${sizemb} MB ${size} bytes"
#done

