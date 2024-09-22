import requests
import os
import sys
import time

os.system('color e')

## URL Of Webhook
url = 'https://discord.com/api/webhooks/1208816366501634068/G-jqa_q82W_fSFQLSo1DehGYRkuH8bng9-DuTeK51OhR3Vn1tpfmG1P0GxTs8qBtlqIO'
# Change This To Your Discord Webhook URL
## Capture Of Text
text = input("Enter The Text" + ": ")
contentofspam = {'content': text}

## Protocol How Many Times You Want To Spam The Webhook
spamprotocol = input("How Many Times You Want To Spam The Webhook?: ")
print("")

## Check For Letters in Spam Protocol
if spamprotocol.isdigit():
    number_requests = 0
    for x in range(int(spamprotocol)):
        x  = requests.post(url, json = contentofspam,)
        number_requests += 1
        print(str(number_requests) + " Messages Transmitted")
else:
    print("")
    print("Only Numbers Are Allowed")
    time.sleep(2)
    sys.exit()



    
    
    
    
    
    
    
    
    
    
    
    
    


