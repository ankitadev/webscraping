from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='/Users/ankitadev/Downloads/chromedriver', chrome_options=option)

for i in range(300000, 400000):
    try:
        print ('\n\n\n')
        print ('********************** COMPANY' , i , '********************')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria=C0" + str(i) + "&SearchSubType=Exact"
        browser.get(business_url)

        #define all the id's in the browser
        titles_element = browser.find_element_by_xpath("//button[@name='EntityId']")
        titles_element.click()

        registration_element = browser.find_elements_by_xpath("//div[@class='col-sm-4 col-xs-6']")
        element = [x.text for x in registration_element]

        registration_key = browser.find_elements_by_xpath("//div[@class='col-sm-8 col-xs-6']")
        key = [x.text for x in registration_key]

        for element, key in zip(element, key):
            print(element + ": " + key, '\n')

    except NoSuchElementException:
        print("Oops!  That was no valid number.  Try again...")
        continue
