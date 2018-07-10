import requests

'''
Lookup Trademarks - 50 max per call

have to feed:
<k>string</k> ----- API Key
<tm>string</fnm> -- Trademark Mark Identification
<tmo>string</lnm> - Trademark Owner Name

'''

url = "https://www.bizapedia.com/bdmservice.asmx?op=LT"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_tm = "something"
name_tmo = "somethings"

xml = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <LT xmlns="https://www.bizapedia.com/">
      <k>{k}</k>
      <tm>{tm}</tm>
      <tmo>{tmo}</tmo>
    </LT>
  </soap12:Body>
</soap12:Envelope>""".format(k=name_k, tm=name_tm, tmo=name_tmo)
headers = {'Content-Type': 'application/soap+xml'}

result = requests.post(url=url, data=xml, headers=headers)

print('STATUS CODE : ', result.status_code, '\n RESPONSE : \n', str(result.content))
