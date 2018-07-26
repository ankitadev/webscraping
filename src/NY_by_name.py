from selenium import webdriver
import collections
from selenium.common.exceptions import NoSuchElementException
import csv
import pdb
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myNameArray = open("Untitled 12.txt").readlines()

for item in myNameArray:
    try:
        print ('\n')
        business_url = "http://corp.sec.state.ma.us/CorpWeb/CorpSearch/CorpSearch.aspx"
        browser.get(business_url)

        inputElement = browser.find_element_by_xpath('//*[@id="MainContent_txtEntityName"]')
        inputElement.send_keys(item)
        inputElement.send_keys(Keys.ENTER)

        titles_element = browser.find_element_by_xpath('//*[@id="MainContent_SearchControl_grdSearchResultsEntity"]/tbody/tr[2]/td[1]/a')
        titles_element.click()

    except NoSuchElementException:
        print("No agent found with this number!!")
        continue