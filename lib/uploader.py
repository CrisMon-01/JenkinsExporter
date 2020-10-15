import requests
import os
import json
import sys
from os.path import isfile, join

def upload (username, token, server) :

    # directoryconfigjob = str(os.getcwd())+"/jobsconfig"
    directoryconfigjob = "./jobsconfig"
    levelpath = ""

    manageUploadJob2Level (levelpath, directoryconfigjob, username, token, server)

def manageUploadJob2Level (levelpath, directory, username, token, server):
    try:
        listfile = os.listdir(directory)
    except: 
        print("[INFO] FOLDER NOT EXISTS")
    
    print ("[INFO] I WILL UPLOAD THE JOBS: "+str(listfile))
    
    allfiles = []
    alldirs = []
    for job in listfile:
        print("[INFO] ADD JOB: "+job)
        if(isfile(directory+'/'+job)) :
            allfiles.append(directory+'/'+job)
        else:
            alldirs.append(directory+'/'+job)
    print("[INFO] FILE LIST: "+str(allfiles)) 
    print("[INFO] DIRECTORY: "+str(alldirs))
    for fileconfig in allfiles: # do all the file first, or you could have problem on the upload in subflder
        print("[INFO] UPLOAD OF: "+fileconfig)
        head, tail = os.path.split(fileconfig)
        job_name = fileconfig.split('.',1)[0]
        short_job_name = tail.split('.',1)[0]
        print("[INFO] JOB NAME: "+short_job_name)
        job_binary = open(fileconfig, 'rb')
        crumb = extractcrumb(username, token, server)
        response = requests.post('http://'+server+levelpath+'/createItem?name='+job_name, auth=(username, token), data=job_binary, headers={'Content-Type': 'text/xml', 'Jenkins-Crumb': crumb})
        if str(response.status_code) != '200':
            print ("[ERR] WRONG POST OF THE JOB (TRY USING TOKEN INSTEAD OF PASSWORD ON 403) :"+str(response.status_code))
        else: 
            print("[INFO] JOB CREATED ON JENKINS :"+str(response.status_code))

    for singledir in alldirs:
        head, tail = os.path.split(singledir)
        levelpath += '/job/'+tail 
        manageUploadJob2Level (levelpath, singledir,username,token,server)

def extractcrumb (username, token, server) : 
    req =  requests.get('http://'+username+':'+token+'@'+server+'/crumbIssuer/api/json')
    response_crumb = req.content.decode('utf-8')
    crumb = json.loads(response_crumb)['crumb']
    print("[INFO] YOU WILL USE THIS CRUMB FOR THE REQUEST: "+crumb)
    return crumb