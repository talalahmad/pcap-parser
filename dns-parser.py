#!/usr/bin/python

import sys
from subprocess import Popen, PIPE

eventlist = []
activeports = {}
dnsqueries = {}
"""
try:
    f = open(sys.argv[1])

except:
    print "Please specify an input file"

line = f.readline()
"""
#-e dns.flags.rcode
cmd = 'tshark -r ' + sys.argv[1] +' -2 -R "dns" -T fields -e frame.time_relative -e ip.src -e ip.dst -e dns.qry.name -e _ws.col.Info'

print cmd


lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]

lines = lines.split('\n')

for line in lines:
	print line
