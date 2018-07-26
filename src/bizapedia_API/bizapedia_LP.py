import requests

'''
Lookup People - 50 max per call

have to feed:
<k>string</k> ----- API Key
<pa>string</pa> --- State
<c>string</c> ----- city
<fnm>string</fnm> - First Name
<lnm>string</lnm> - Last Name
      
'''

url = "https://www.bizapedia.com/bdmservice.asmx?op=LP"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_pa = "DE"
name_c = "D"
name_fnm = "something"
name_lnm = "somethings"
name_n = "Dropbox"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <LP xmlns="https://www.bizapedia.com/">
      <k>{k}</k>
      <fnm>{fnm}</fnm>
      <lnm>{lnm}</lnm>
      <c>{c}</c>
      <pa>{pa}</pa>
    </LP>
  </soap12:Body>
</soap12:Envelope>""".format(k=name_k,pa=name_pa,fnm=name_fnm,lnm=name_lnm,c=name_c)
headers = {'Content-Type': 'application/soap+xml'}

result = requests.post(url=url,data=xml,headers=headers)

print('STATUS CODE : ',result.status_code, '\n RESPONSE : \n', str(result.content))
