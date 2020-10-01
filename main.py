import sys
import getpass
from lib import extractor
from lib import uploader
from lib import installer

username = ''
token = ''
server = ''
action = ''

if len(sys.argv)<=3:
    username = input("[INFO] ENTER JENKINS USERNAME: ")
    token = getpass.getpass("[INFO] ENTER TOKEN/PASSWORD: ")
    server = input("[INFO] ENTER SERVER URL + PORT (NO HTTP://): ")
    action = input("[INFO] ENTER METHOD: ")
else:
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
        action = sys.argv[(len(sys.argv)-1)]

print("[INFO] AUTH:"+username+" "+token+' @ SERVER: '+server)

if action == 'download':
    print("[INFO] YOU WILL DOWNLOAD JOB'S CONFIG FILE")
    extractor.extraction(username,token,server)
else: 
    if action == 'upload':
        print("[INFO] YOU WILL UPLOAD JOB'S CONFIG FILE")
        uploader.upload(username,token,server)
    else:
        if action == 'installplugin':
            print("[INFO] YOU WILL INSTALL LUGIN IN THE PLUGINS FOLDER")
            installer.install(username,token,server)
        else:
            print("[WARN] YOU HAVEN'T SPECIFY ACTION")
            sys.exit()