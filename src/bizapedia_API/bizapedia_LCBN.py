import requests

'''
Lookup company by company name, you will get only one company 

have to feed:
<k>string</k> ---- API Key
<pa>string</pa> -- State
<n>string</n> ---- Name of the company

'''
myNameArray = open("Untitled 10.txt").readlines()
url = "https://www.bizapedia.com/bdmservice.asmx?op=LCBN"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_pa = "DE"
name_n = "Dropbox"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">  <soap12:Body>
    <LCBN xmlns="https://www.bizapedia.com/">
      <k>{k}</k>
      <n>{n}</n>
      <pa>{pa}</pa>
    </LCBN>
  </soap12:Body>
</soap12:Envelope>""".format(k=name_k,n=name_n,pa=name_pa)
headers = {'Content-Type': 'application/soap+xml'}

result = requests.post(url=url,data=xml,headers=headers)

print('STATUS CODE : ',result.status_code, '\n RESPONSE : \n', str(result.content))
