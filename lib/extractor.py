import requests
import xml.etree.ElementTree as ET
import sys
import os

def extraction (username, token, server):

    try:
        os.makedirs('./jobsconfig')
    except: 
        print("[INFO] FOLDER ALREADY")

    response_xml = requests.get('http://'+username+':'+token+'@'+server+'/view/All/api/xml?')
    xmlAlljobs = ET.fromstring(str(response_xml.text))
    listjobs = []
    for child in xmlAlljobs:
        if child.tag != 'name' :
            if child.tag != 'url':
                try:
                    listjobs.append(child[0].text)
                except: 
                    print("[WARN] CAN'T CREATE ")
    print("[INFO] JOB LIST: "+str(listjobs))
    for job in listjobs:
        configjob = requests.get('http://'+username+':'+token+'@'+server+'/job/'+str(job)+'/config.xml')
        print("[INFO] YOU WILL DOWNLOAD JOB: "+job)
        print(str(configjob.text))
        fileconfig = open('./jobsconfig/'+job+'.xml', 'w+')
        fileconfig.write(configjob.text)
