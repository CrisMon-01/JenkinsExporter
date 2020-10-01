import requests
import os

def install (username, token, server) :

    try:
        listfile = os.listdir('./plugins')
    except: 
        print("[INFO] FOLDER NOT EXISTS")