import requests

'''
Lookup company by File number, you will get only one company 

have to feed:
<k>string</k> ---- API Key
<pa>string</pa> -- State
<fn>string</fn> ---- File Number

'''

url = "https://www.bizapedia.com/bdmservice.asmx?op=LCBFN"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_pa = "DE"
name_fn = "CS3000000"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <LCBFN xmlns="https://www.bizapedia.com/">
      <k>{k}</k>
      <pa>{pa}</pa>
      <fn>{fn}</fn>
    </LCBFN>
  </soap12:Body>
</soap12:Envelope>""".format(k=name_k,pa=name_pa,fn=name_fn)
headers = {'Content-Type': 'application/soap+xml'}

result = requests.post(url=url,data=xml,headers=headers)

print('STATUS CODE : ',result.status_code, '\n RESPONSE : \n', str(result.content))