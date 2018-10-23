#!/usr/bin/python

import sys
from subprocess import Popen, PIPE



cmd = 'tshark -r ' + sys.argv[1] +' -2 -R "http.request || http.response" -T fields -e frame.time_relative -e ip.src -e ip.dst -e frame.protocols -e http.request.uri -e http.response.code'

print cmd


lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]

lines = lines.split('\n')

for line in lines:
    print line

