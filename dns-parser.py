import sys
from subprocess import Popen, PIPE


#-e dns.flags.rcode
folders = 't-mobile_android  t-mobile_firefox  verizon_firefox  wired_android  wired_firefox'
folders = folders.split() # folders variable is now an array that contains all folder names 
files = 'adobe.com,cnn.com,qq.com,twitter.com,amazon.com,google.com,rakuten.co.jp,aol.com,microsoft.com,taobao.com'
files = files.split(',')

cmd = 'tshark -r ' + sys.argv[1] +' -2 -R "dns" -T fields -e frame.time_relative -e ip.src -e ip.dst -e dns.qry.name -e _ws.col.Info'

print cmd


lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]

lines = lines.split('\n')

for line in lines:
	print line
	#this line seperates line into columns
	columns = line.split("\t")
	time = columns[0]
	dns_query_name = columns[3]



#Hint: -e dns.qry.name is the key that will be common in the dns query and response so it can be used to match a query to its response 
