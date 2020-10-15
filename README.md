# Simple Jenkins tool to manage migration between servers and users

I use this to move jenkins job between users and servers. <br>

## Require
* python3 
    * requests
    * xml.etree.ElementTree as ET
    * sys
    * os
    * getpass
    * jenkins
    * python-jenkins
    * json
    * yaml
* Jenkins credential
    * user
    * token/password [In Jenkins you can create one on: User (up, right in the main page) -> Configure -> Token API]
        * please use the token for the upload, the password has some problem with the CSFR security
    * server

## Run: 
`python3 main.py -n=$user -t=$api -s=$server $action` <br>
The last parameter is the action you want to do: download config job or upload that (for the other parameter there is no real order. 
or <br>
`python3 main.py` or <br>
`python3 main.py --auth-file` <br>
In this case, you need to create a file named: credential.yaml in the config folder: `./config/credential.yaml` with this field:
* jenkins_username
* jenkins_token
* jenkins_server
* jenkins_port
* action

<br>
* download: job from your old server/user
* upload: on the new user/server
* list-plugin: list the plugin from th eserver in json format (./config/plugins.json)

# TO-DO:
?