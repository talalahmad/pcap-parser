import matplotlib.pyplot as plt
import sys
from subprocess import Popen, PIPE

dnsqueries = {}
order = []

#-e dns.flags.rcode
folders = 't-mobile_android  t-mobile_firefox  verizon_firefox  wired_android  wired_firefox'
folders = folders.split() # folders variable is now an array that contains all folder names 
files = 'adobe.com,cnn.com,qq.com,twitter.com,amazon.com,google.com,rakuten.co.jp,aol.com,microsoft.com,taobao.com'
files = files.split(',')

current_file = "pcaps/"+folders[0]+"/*"+files[1]+"*.pcap"

cmd = 'tshark -r ' + current_file +' -2 -R "dns" -T fields -e frame.time_relative -e ip.src -e ip.dst -e dns.qry.name -e dns.flags.rcode -e _ws.col.Info'

print cmd


lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode('utf-8')
#lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]

lines = lines.split('\n')

for line in lines:
	#print line
	#this line seperates line into columns
	columns = line.split("\t")
	if columns == ['']:
		continue
	time = columns[0]
	#print columns
	dns_query_name = columns[3]
	dns_query_flag = columns[4]
	if dns_query_flag == '':
		#this is actually not correct way to do this, it needs to be improved 
		#this works to show what is going on
		#what I am doing here is that if I say a new name, I count that as a new DNS query 
		#and everytime I see that name again I just treat that as a reply to the query 
		#but it can be a refused request and means you will send it again  
		if dns_query_name not in dnsqueries.keys(): 
			dnsqueries[dns_query_name] = {"queries":[],"replies":[],"name":dns_query_name}
			dnsqueries[dns_query_name]["queries"].append(time)
			order.append(dns_query_name)
		else: 
			dnsqueries[dns_query_name]["replies"].append((dns_query_flag,time))

plt.xlabel('time (seconds)')

yticks = []
xpoints = []

for dnsquery in order:
	#print dnsquery
	yticks.append("DNSQUERY for "+ dnsquery)

print yticks

yticknums = list(range(len(yticks)))

yticknums.reverse()

plt.yticks(yticknums,yticks)

en = enumerate(order)
for idx,key in en:
	current_y = [len(dnsqueries) - idx -1]
	querytimes = [float(x) for x in dnsqueries[key]["queries"]]
	responsetimes = [float(x[1]) for x in dnsqueries[key]["replies"]]
	responseflags = [x[0] for x in dnsqueries[key]["replies"]]

	timepts = querytimes+responsetimes
	plt.plot(timepts,current_y*len(timepts), "bo-")
	

plt.ylim(ymin=-1, ymax=len(yticks)+1)

plt.show()








#Hint: -e dns.qry.name is the key that will be common in the dns query and response so it can be used to match a query to its response 
