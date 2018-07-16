import urllib
from selenium import webdriver
import collections
from selenium.common.exceptions import NoSuchElementException
import csv

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myFileNumberArray = open("california_names.txt").readlines()

for item in myFileNumberArray:
    try:
        print ('\n')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria=" + item
        browser.get(business_url)

        # define all the id's in the browser
        titles_element = browser.find_element_by_xpath("//button[@name='EntityId']")
        titles_element.click()

        registration_key = browser.find_elements_by_xpath("//button[@class='btn btn-link docImage']")

        for i in len(registration_key):
            pdf_url = registration_key[i].get_attribute("value")
            urllib.urlretrieve(pdf_url, "California_" + item + "_type.pdf")

    except NoSuchElementException:
        print("No PDF found in this page!!")
        continue
