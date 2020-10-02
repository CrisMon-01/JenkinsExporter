# Simple Jenkins tool to manage migration between servers and users

I use this to move jenkins job between users and servers. <br>

## Require
* python3 
    * requests
    * xml.etree.ElementTree as ET
    * sys
    * os
    * getpass
* Jenkins credential
    * user
    * token/password [In Jenkins you can create one on: User (up, right in the main page) -> Configure -> Token API]
        * please use the token for the upload, the password has some problem with the CSFR security
    * server

## Run: 
`python3 main.py -n=$user -t=$api -s=$server $action`
or <br>
`python3 main.py`
The last parameter is the action you want to do: download config job or upload that (for the other parameter there is no real order. <br>
* download: job from your old server/user
* upload: on the new user/server

# TO-DO:
* use config file for the credential
* update to manage job in sub folder (now it take all the job in the "home" of Jenkins)
