import cloudscraper
import sys
import json
import requests

sAKCContent = "";

with open ("ankama-accounts.txt", "r") as myfile:
    sAKCContent = myfile.read().replace('\n', ':')

sAKCContent = str.split(sAKCContent, ':')
iAccountId = 0
sAccountsFR = ""

while iAccountId < len(sAKCContent) - 1 :
    scraper = cloudscraper.create_scraper() # returns a CloudScraper instance
    uri = "https://haapi.ankama.com/json/Ankama/v2/Api/CreateApiKey"

    print(sAKCContent[iAccountId] + ":" + sAKCContent[iAccountId + 1])
        
    data = {'login':sAKCContent[iAccountId], 
            'password':sAKCContent[iAccountId + 1], 
            'long_life_token':False}

    result = scraper.post(url=uri,data=data)
    dataJson = json.loads(result.text)

    if dataJson.get('key') != None and dataJson['data']['country'] == "FR":
        sAccountsFR = sAccountsFR + sAKCContent[iAccountId] + ":" + sAKCContent[iAccountId + 1] + "\n"
        print("+Ajouté")
    else:
        print(result)
    iAccountId = iAccountId + 2

f = open("FR" + str(int(time.time())) +".txt", "a")
f.write(sAccountsFR)
print("Done")
f.close()
