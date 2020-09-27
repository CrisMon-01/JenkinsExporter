import requests
import xml.etree.ElementTree as ET
import sys
import os

username = ''
token = ''
server = ''

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

print("[INFO] AUTH:"+username+':'+token)

try:
    os.makedirs('jobsconfig')
except: 
    print("[INFO] CARTELLA PRESENTE")

response_xml = requests.get('http://'+username+':'+token+'@'+server+'/view/All/api/xml?')
xmlAlljobs = ET.fromstring(str(response_xml.text))
listjobs = []
for child in xmlAlljobs:
    if child.tag != 'name' :
        if child.tag != 'url':
            try:
                listjobs.append(child[0].text)
            except: 
                print("[INFO] ECCEZIONE")
print("[INFO] JOB LIST: "+str(listjobs))
for job in listjobs:
    configjob = requests.get('http://'+username+':'+token+'@'+server+'/job/'+str(job)+'/config.xml')
    print(str(configjob.text))
    fileconfig = open('./jobsconfig/'+job+'.xml', 'w+')
    fileconfig.write(configjob.text)
