import time
import requests
## Url Of The Webhook
url = 'Add Your Webhook URL'


drp = input("Enter The Text" + ":")
contentofspam = {'content': drp}

print("Made By DrPanayioths For Testing Purposes")
time.sleep(5)

## Change The Number after the range for the Spam
for x in range(15):
    x  = requests.post(url, json = contentofspam,)