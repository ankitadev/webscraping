import urlparse
import urllib2
import os
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

for i in range(300000, 400000):
    try:
        print ('\n\n\n')
        print ('********************** page', i, '********************')
        download_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria=C0" + str(i) + "&SearchSubType=Exact"
        browser.get(download_url)

    except NoSuchElementException:
        print("No PDF found in this page!!")
        continue
