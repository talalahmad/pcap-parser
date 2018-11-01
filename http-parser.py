#!/usr/bin/python

import sys
from subprocess import Popen, PIPE
folders = 't-mobile_android  t-mobile_firefox  verizon_firefox  wired_android  wired_firefox'
folders = folders.split() # folders variable is now an array that contains all folder names 
files = 'adobe.com,cnn.com,qq.com,twitter.com,amazon.com,google.com,rakuten.co.jp,aol.com,microsoft.com,taobao.com'
files = files.split(',')


cmd = 'tshark -r ' + sys.argv[1] +' -2 -R "http.request || http.response" -T fields -e frame.time_relative -e ip.src -e ip.dst -e frame.protocols -e http.request.uri -e http.response.code'

print cmd


lines = Popen(cmd, shell=True, stdout=PIPE).communicate()[0]

lines = lines.split('\n')

for line in lines:
    print line

