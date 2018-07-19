import requests
import xml.etree.ElementTree as ET
import csv

'''
Lookup company by company name, you will get only one company 

have to feed:
<k>string</k> ---- API Key
<pa>string</pa> -- State
<n>string</n> ---- Name of the company

'''
myNameArray = open("domestic_delaware.txt").readlines()
url = "https://www.bizapedia.com/bdmservice.asmx?op=LCBN"
name_k = "ZVJDKQEVOZOMJBDJCG"
name_pa = "DE"

for ite in myNameArray:
    print ("COMPANY NAME: ", ite)
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

    #print('STATUS CODE : ',result.status_code, '\n RESPONSE : \n', str(result.content))

    tree = ET.fromstring(str(result.content))

    company = tree.findall('.//{https://www.bizapedia.com/}Company')
    print ("COUNT: ", len(company))

    with open('COUNT_ALL_DOVER_BIzapedia.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow([ite]  + [str(len(company))])
    csvfile.close()

    for item in tree.iter('{https://www.bizapedia.com/}Company'):
        print ("hello loop")
        x1 = item.find('{https://www.bizapedia.com/}EntityName').text  # Company Name
        x2 = item.find('{https://www.bizapedia.com/}FileNumber').text  # File Number
        x3 = item.find('.//{https://www.bizapedia.com/}FilingJurisdictionName').text  # Filed State
        x4 = item.find('.//{https://www.bizapedia.com/}FilingJurisdictionPostalAbbreviation').text  # state
        x5 = item.find('.//{https://www.bizapedia.com/}DomesticJurisdictionName').text
        x6 = item.find('.//{https://www.bizapedia.com/}DomesticJurisdictionPostalAbbreviation').text
        x7 = item.find('.//{https://www.bizapedia.com/}FilingStatus').text  # Filing status
        x8 = item.find('.//{https://www.bizapedia.com/}EntityType').text  # Entity Type
        x9 = item.find('.//{https://www.bizapedia.com/}FilingDate').text  # Filing Date
        x10 = item.find('.//{https://www.bizapedia.com/}PrincipalAddressCountryCode').text
        x11 = item.find('.//{https://www.bizapedia.com/}PrincipalAddressLine1').text
        x12 = item.find('.//{https://www.bizapedia.com/}PrincipalAddressLine2').text
        x13 = item.find('.//{https://www.bizapedia.com/}PrincipalAddressCity').text
        x14 = item.find('.//{https://www.bizapedia.com/}PrincipalAddressState').text
        x15 = item.find('.//{https://www.bizapedia.com/}PrincipalAddressPostalCode').text
        x16 = item.find('.//{https://www.bizapedia.com/}MailingAddressCountryCode').text
        x17 = item.find('.//{https://www.bizapedia.com/}MailingAddressLine1').text
        x18 = item.find('.//{https://www.bizapedia.com/}MailingAddressLine2').text
        x19 = item.find('.//{https://www.bizapedia.com/}MailingAddressCity').text
        x20 = item.find('.//{https://www.bizapedia.com/}MailingAddressState').text
        x21 = item.find('.//{https://www.bizapedia.com/}MailingAddressPostalCode').text
        x22 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentName').text  # Registered Agent Name
        x23 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentAddressCountryCode').text  # Registered Agent Address C ountry Code
        x24 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentAddressLine1').text  # Registered Agent Address Line1
        x25 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentAddressLine2').text
        x26 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentCity').text  # Registered Agent City
        x27 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentState').text  # Registered Agent State
        x28 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentPostalCode').text  # Registered Agent Postal Code
        x29 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentPhone').text
        x30 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentFax').text
        x31 = item.find('.//{https://www.bizapedia.com/}RegisteredAgentEmail').text
        x32 = item.find('.//{https://www.bizapedia.com/}LastUpdateDate').text  # Last Update Date
        x33 = item.find('.//{https://www.bizapedia.com/}RelevanceScore').text  # Relevance Score

        with open('DOVER_Stanford_All_BIzapedia.csv', 'a') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(
                [x1] + [x2] + [x3] + [x4] + [x5] + [x6] + [x7] + [x8] + [x9] + [x10] + [x11] + [x12] + [x13] + [x14] + [
                    x15] + [x16] + [x17] + [x18] + [x19] + [x20] + [x21] + [x22] + [x23] + [x24] + [x25] + [x26] + [
                    x27] + [x28] + [x29] + [x30] + [x31] + [x32] + [x33])
        csvfile.close()
