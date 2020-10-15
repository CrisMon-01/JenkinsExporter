import requests
import xml.etree.ElementTree as ET
import os

def extraction (username, token, server):

    directoryconfigjob = "./jobsconfig"
    levelpath = ""

    try:
        os.makedirs(directoryconfigjob)
    except: 
        print("[INFO] FOLDER ALREADY")
    manageDownloadJob2Level(levelpath,directoryconfigjob, username, token, server)

def manageDownloadJob2Level (levelpath, directory, username, token, server):
    response_xml = requests.get('http://'+username+':'+token+'@'+server+levelpath+'/view/All/api/xml?')
    xmlAlljobs = ET.fromstring(str(response_xml.text))
    listajob_folder = []
    for child in xmlAlljobs:
        if child.tag != 'name' :
            if child.tag != 'url':
                try:
                    listajob_folder.append(child[0].text)
                except: 
                    print("[WARN] CAN'T CREATE ")
    levelhavefolder = False
    currentdir = directory
    print("[INFO] YOU'RE WOKING IN: "+str(currentdir))
    for job in listajob_folder:
        configjob = requests.get('http://'+username+':'+token+'@'+server+levelpath+'/job/'+str(job)+'/config.xml')
        print("[INFO] YOU WILL DOWNLOAD JOB: "+str(job))
        fileconfig = open(currentdir+'/'+str(job)+'.xml', 'w+')
        fileconfig.write(configjob.text)
        if ("plugin=\"cloudbees-folder@" in str(configjob.text)):
            levelhavefolder = True
            levelpath+='/job/'+str(job)
            directory+='/'+str(job)
            try:
                os.makedirs(directory)
            except: 
                print("[INFO] FOLDER ALREADY")
    if (levelhavefolder):
        manageDownloadJob2Level(levelpath, directory, username, token, server)
