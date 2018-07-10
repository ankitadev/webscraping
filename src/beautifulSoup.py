from bs4 import BeautifulSoup
from HTMLParser import HTMLParseError

for i in range(303928, 400000):
    try:
        print ('\n')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria=C0" + str(i) + "&SearchSubType=Exact"
        soup = BeautifulSoup(business_url, 'html.parser')

    except HTMLParseError:
        print("No agent found with this number!!")
        continue
