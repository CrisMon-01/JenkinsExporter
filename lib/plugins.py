import requests
import os
import jenkins
import json

def makelist (user, token, server) :
    server_jenkins = jenkins.Jenkins('http://'+server, username=user, password=token)
    plugins = server_jenkins.get_plugins_info()
    with open('./config/plugins.json', 'w') as outfile:
        json.dump(plugins, outfile, indent=4)