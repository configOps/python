while read ip; 
do
       echo $ip
       nmap $ip >>"hello.txt"
       echo "################################" >> "hello.txt"
done < "Output.txt"
