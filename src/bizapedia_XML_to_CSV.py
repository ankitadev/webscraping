import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.bizapedia.com/bdmservice.asmx?op=LCSBN"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_pa = "DE"
name_c = "Dover"
name_n = "Genscape, Inc."

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

print('STATUS CODE : ',result.status_code, '\n RESPONSE : \n', str(result.content))

f = open('company.csv', 'a')
csvwriter = csv.writer(f)
count = 0

head = ['Entity Name','File Number','State','Filing Status','Entity Type','Filing Date','Agent Name','Street','Address Line two','City','State','Postal Code','Country']
csvwriter.writerow(head)

soup = BeautifulSoup(result.content,'xml')

for info in soup.find_all('LCBNResult'):
    row = []
    entity_name = info.find('EntityName').text
    row.append(entity_name)


    print entity_name
    file_number = info.find('FileNumber').text
    row.append(file_number)

    print (file_number)
    state = info.find('FilingJurisdictionPostalAbbreviation').text
    row.append(state)
    filing_status = info.find('FilingStatus').text
    row.append(filing_status)
    entity_type = info.find('EntityType').text
    row.append(entity_type)
    filing_date = info.find('FilingDate').text
    row.append(filing_date)
    agent_name = info.find('RegisteredAgentName').text
    row.append(agent_name)
    street = info.find('PrincipalAddressLine1').text
    row.append(street)
    street_two = info.find('PrincipalAddressLine2').text
    row.append(street_two)
    city = info.find('PrincipalAddressCity').text
    row.append(city)
    address_state = info.find('PrincipalAddressState').text
    row.append(address_state)
    zip_code = info.find('PrincipalAddressPostalCode').text
    row.append(zip_code)
    country = info.find('MailingAddressCountryCode').text
    row.append(country)

    csvwriter.writerow(row)

f.close()


