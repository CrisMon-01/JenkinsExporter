import sys
import getpass
import yaml
import logging
from lib import extractor
from lib import uploader
from lib import plugins

username = ''
token = ''
server = ''
action = ''
try:
    os.remove("./logs/result.log")
    fh = logging.FileHandler('./logs/result.log')
except:
    fh = logging.FileHandler('./logs/result.log')

logger = logging.getLogger('MAIN')
logger.setLevel(logging.DEBUG)
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

if len(sys.argv)<=2:
    if '--auth-file' in sys.argv:
        configinfo = yaml.load(open('./config/credential.yaml'))
        username = configinfo['jenkins_username']
        token = configinfo['jenkins_token']
        server = configinfo['jenkins_server']+':'+str(configinfo['jenkins_port'])
        action = configinfo['action']
    else:
        username = input("[INFO] ENTER JENKINS USERNAME: ")
        token = getpass.getpass("[INFO] ENTER TOKEN/PASSWORD: ")
        server = input("[INFO] ENTER SERVER URL + PORT (NO HTTP://): ")
        action = input("[INFO] ENTER METHOD: ")
else:
    for arg in sys.argv:
        if '-n=' in arg:
            username = arg[3:]
        if '-t=' in arg:
            token = arg[3:]
        if '-s=' in arg:
            server = arg[3:]
        action = sys.argv[(len(sys.argv)-1)]

logging.debug('USER: '+username)
logging.debug('TOKEN: '+token)
logging.debug('ACTION: '+action)

print("[INFO] AUTH:"+username+" "+token+' @ SERVER: '+server)

if action == 'download':
    logger.debug("YOU WILL DOWNLOAD JOB'S CONFIG FILE")
    print("[INFO] YOU WILL DOWNLOAD JOB'S CONFIG FILE")
    extractor.extraction(username,token,server)
else: 
    if action == 'upload':
        logger.debug("YOU WILL UPLOAD JOB'S CONFIG FILE")
        print("[INFO] YOU WILL UPLOAD JOB'S CONFIG FILE")
        uploader.upload(username,token,server)
    else:
        if action == 'list-plugin':
            logger.debug("LIST THE PLUGIN OF THE JENKINS @ "+server+" IN config/plugin.json")
            print("[INFO] I WILL LIST THE PLUGIN OF THE JENKINS @ "+server+" IN config/plugin.json")
            try:
                plugins.makelist(username,token,server)
                logger.debug("CHECK config/plugin.json")
            except:
                logger.error("ERROR IN MAKELIST ")
        else:
            print("[WARN] YOU HAVEN'T SPECIFY ACTION")
            logger.error("NO PARAMS")
            sys.exit()