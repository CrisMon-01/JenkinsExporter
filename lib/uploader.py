import requests
import os

def upload (username, token, server) :

    try:
        listfile = os.listdir('./jobsconfig')
    except: 
        print("[INFO] FOLDER NOT EXISTS")

    print ("[INFO] I WILL UPLOAD THE JOB: "+str(listfile))
    
    for job in listfile:
        print("[INFO] UPLOAD OF: "+job)
        job_name = job.split('.',1)[0]
        job_binary = open('./jobsconfig/'+job, 'rb')
        response = requests.post('http://'+server+'/createItem?name='+job_name, auth=(username, token), data=job_binary, headers={'Content-Type': 'text/xml'})
        if str(response.status_code) != '200':
            print ("[ERR] WRONG POST OF THE JOB (TRY USING TOKEN INSTEAD OF PASSWORD ON 403) :"+str(response.status_code))
        else: 
            print("[INFO] JOB CREATED ON JENKINS :"+str(response.status_code))