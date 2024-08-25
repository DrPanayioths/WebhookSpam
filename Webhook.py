import requests

## URL Of Webhook
url = 'Change This To Your Discord Webhook URL'

## Capture Of Text
text = input("Enter The Text" + ": ")
contentofspam = {'content': text}

## Protocol How Many Times You Want To Spam The Webhook
spamprotocol = input("How Many Times You Want To Spam The Webhook?: ")

## Change From String To Integer
spamprotocol = int(spamprotocol)

## Change The Number after the range for the Spam
number_requests = 0
for x in range(int(spamprotocol)):
    x  = requests.post(url, json = contentofspam,)
    number_requests += 1
    print(str(number_requests) + " Messages Transmitted")
    
    
    
    
    
    
    
    
    
    
    
    
    


