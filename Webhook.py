import sys
import time
import subprocess


## Automatically Install The Requests Package:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])

import requests


## Url Of The Webhook
url = 'Change With Webhook URL'

## Input The Text To System For Testing Purpose
drp = input("Enter The Text" + ": ")
contentofspam = {'content': drp}

## Print Credits
print("Made By DrPanayioths For Testing Purposes")
time.sleep(5)

## Protocol How Many Times You Want To Spam The Webhook
spamprotocol = input("How Many Times You Want To Spam The Webhook? ")

## Change From String To Integer
spamprotocol = int(spamprotocol)

## Change The Number after the range for the Spam
for x in range(int(spamprotocol)):
    x  = requests.post(url, json = contentofspam,)
    
    
    
    
    
    
    
    
    
    
    
    
    


