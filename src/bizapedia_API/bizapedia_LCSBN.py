import requests

'''
Lookup Companies - 50 max per call

have to feed:
<k>string</k> ---- API Key
<pa>string</pa> -- State
<n>string</n> ---- Name of the company
<c>string</c> ---- city

'''
myNameArray = open("domestic_delaware.txt").readlines()

url = "https://www.bizapedia.com/bdmservice.asmx?op=LCSBN"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_pa = "DE"
name_c = "Dover"
name_n = "Something"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <LCSBN xmlns="https://www.bizapedia.com/">
      <k>{k}</k>
      <n>{n}</n>
      <pa>{pa}</pa>
      <c>{c}</c>
    </LCSBN>
  </soap12:Body>
</soap12:Envelope>""".format(k=name_k,n=name_n,c=name_c,pa=name_pa)
headers = {'Content-Type': 'application/soap+xml'}

result = requests.post(url=url,data=xml,headers=headers)