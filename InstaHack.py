import sys
import time
import requests
import subprocess


## Automatically Install The Requests Package:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'requests'])

## Url Of The Webhook
url = 'Add Your Webhook URL'


drp = input("Enter The Text" + ":")
contentofspam = {'content': drp}

print("Made By DrPanayioths For Testing Purposes")
time.sleep(5)

spamprotocol = input("How Many Times You Want To Spam The Webhook?")

spamprotocol = int(spamprotocol)

## Change The Number after the range for the Spam
for x in range(int(spamprotocol)):
    x  = requests.post(url, json = contentofspam,)
    
    
    
    
    
    
    


