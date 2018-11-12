#!/usr/bin/python

import sys
from subprocess import Popen, PIPE
import matplotlib.pyplot as plt


folders = 't-mobile_android  t-mobile_firefox  verizon_firefox  wired_android  wired_firefox'
folders = folders.split() # folders variable is now an array that contains all folder names 
files = 'adobe.com,cnn.com,qq.com,twitter.com,amazon.com,google.com,rakuten.co.jp,aol.com,microsoft.com,taobao.com'
files = files.split(',')


current_file = "pcaps/"+folders[0]+"/*"+files[1]+"*.pcap"


cmd = 'tshark -r ' + current_file +' -2 -R "http.request || http.response" -T fields -e frame.time_relative -e ip.src -e ip.dst -e frame.protocols -e http.request.uri -e http.response.code -e tcp.srcport -e tcp.dstport'

print cmd

order = []
activeports = {}


lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0].decode('utf-8')

lines = lines.split('\n')

for line in lines:
    print line

    columns = line.split('\t')

    time = columns[0]
    if columns == ['']:
    	continue

    if columns[4] != '':
    	order.append({"type": "GET",
    		"starttime": time,
    		"end": None,
    		"response":None,
    		"resource": columns[4],
    		"localport":columns[6]})
    	activeports[columns[6]] = order[len(order)-1]

    if columns[5] != '':
    	#this is a response
        responsecode = columns[5]
        dstport = columns[7] 
        activeports[dstport]["end"] = time
        activeports[dstport]["response"] = responsecode


plt.xlabel('time (seconds)')

yticks = []
xpoints = []
for event in order:
    if event["type"] == "GET":
        yticks.append("GET " + event["resource"][-10:])
        print event["end"], event["starttime"]

        if event["end"] != None:
            xpoints += [float(event["starttime"]), float(event["end"])]
        #Orphaned GETS will only be a point
        else:
            xpoints += [float(event["starttime"]), float(event["starttime"])]

  


print yticks

yticknums = list(range(len(yticks)))
yticknums.reverse()

plt.yticks(yticknums, yticks)
print yticknums, yticks


for idx, event in enumerate(order):
    current_y = [len(order) - idx - 1]
    if event["type"] == "GET":
        #XXX: Violating DRY principle
        if event["end"] != None:
            plt.plot([float(event["starttime"]), float(event["end"])], current_y*2, "go-")
        else:
            plt.plot([float(event["starttime"]), float(event["starttime"])], current_y*2, "go-")



plt.show()