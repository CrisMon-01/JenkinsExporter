import requests
import xml.etree.ElementTree as ET
import sys
import os

from lib import extractor

username = ''
token = ''
server = ''
action = ''

for arg in sys.argv:
    if '-n=' in arg:
        username = arg[3:]
        print("[INFO] USER:"+username)
    if '-t=' in arg:
        token = arg[3:]
        print("[INFO] TOKEN:"+token)
    if '-s=' in arg:
        server = arg[3:]
        print("[INFO] TOKEN:"+server)

print("[INFO] AUTH:"+username+token+' @ SERVER: '+server)

if sys.argv[(len(sys.argv)-1)] == 'download':
    print("[INFO] YOU WILL DOWNLOAD JOB'S CONFIG FILE")
    extractor.extraction(username,token,server)
else: 
    if  sys.argv[(len(sys.argv)-1)] == 'upload':
        print("[INFO] YOU WILL UPLOAD JOB'S CONFIG FILE")
    else:
        print("[INFO] YOU WILL DOWNLOAD JOB'S CONFIG FILE")
        extractor.extraction(username,token,server)