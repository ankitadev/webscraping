import requests

'''
Lookup Addresses - 50 max per call

have to feed:
<k>string</k> ----- API Key
<a>string</a> ----- Address
<c>string</c> ----- City
<pa>string</pa> ----- State
<pc>string</pc> ----- Postal code

'''

url = "https://www.bizapedia.com/bdmservice.asmx?op=LA"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_a = "120 peters st"
name_c = "Drover"
name_pa = "DE"
name_pc = "02139"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <LA xmlns="https://www.bizapedia.com/">
      <k>{k}</k>
      <a>{a}</a>
      <c>{c}</c>
      <pa>{pa}</pa>
      <pc>{pc}</pc>
    </LA>
  </soap12:Body>
</soap12:Envelope>""".format(k=name_k, a=name_a, c=name_c, pa=name_pa, pc=name_pc)
headers = {'Content-Type': 'application/soap+xml'}

result = requests.post(url=url, data=xml, headers=headers)

print('STATUS CODE : ', result.status_code, '\n RESPONSE : \n', str(result.content))
