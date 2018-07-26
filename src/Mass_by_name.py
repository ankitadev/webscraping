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

        titles_element = browser.find_element_by_xpath(
            '//*[@id="MainContent_SearchControl_grdSearchResultsEntity"]/tbody/tr[2]/td[1]/a')
        titles_element.click()

        # all the text elements
        comp_name = browser.find_element_by_xpath('//*[@id="MainContent_lblEntityName"]').text
        entity_type = browser.find_element_by_xpath('//*[@id="MainContent_lblEntityType"]').text
        file_num = browser.find_element_by_xpath('//*[@id="MainContent_lblIDNumberHeader"]').text
        register_date = browser.find_element_by_xpath('//*[@id="MainContent_lblOrganisationDate"]').text
        withdrawal_date = browser.find_element_by_xpath('//*[@id="MainContent_lblInactiveDate"]').text
        organized_under = browser.find_element_by_xpath('//*[@id="MainContent_lblJurisdiction"]').text
        principal_address = browser.find_element_by_xpath('//*[@id="MainContent_trConfPrinciple1"]/td[2]').text
        add_city = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleCity"]').text
        add_zip = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleZip"]')
        add_country = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleCountry"]')
        add_state = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleState"]')

        agent_name = browser.find_element_by_xpath('//*[@id="MainContent_tblResident"]/tbody/tr[3]/td[2]')
        agent_address = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentStreet"]')
        agent_city = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentCity"]').text
        agent_zip = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentZip"]')
        agent_country = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentCountry"]')
        agent_state = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentState"]')

        view_filings = browser.find_element_by_xpath('//*[@id="MainContent_btnViewFilings"]')
        view_filings.click()




    except NoSuchElementException:
        print("No agent found with this number!!")
        continue