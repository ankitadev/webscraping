from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import pdb

from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myNameArray = open("Untitled 12.txt").readlines()


def variables():
    # all the text elements
    try:
        comp_name = browser.find_element_by_xpath('//*[@id="MainContent_lblEntityName"]').text
        entity_type = browser.find_element_by_xpath('//*[@id="MainContent_lblEntityType"]').text
        file_num = browser.find_element_by_xpath('//*[@id="MainContent_lblIDNumberHeader"]').text
        register_date = browser.find_element_by_xpath('//*[@id="MainContent_lblOrganisationDate"]').text
        withdrawal_date = browser.find_element_by_xpath('//*[@id="MainContent_lblInactiveDate"]').text
        organized_under = browser.find_element_by_xpath('//*[@id="MainContent_lblJurisdiction"]').text
        x1 = organized_under.replace("Organized under the laws of: State: ", "")
        filed_under_state = x1[0:2]
        filed_on_date = x1[20:]

        principal_address = browser.find_element_by_xpath('//*[@id="MainContent_trConfPrinciple1"]/td[2]').text
        add_city = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleCity"]').text
        add_zip = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleZip"]').text
        add_country = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleCountry"]').text
        add_state = browser.find_element_by_xpath('//*[@id="MainContent_lblPrincipleState"]').text

        agent_name = browser.find_element_by_xpath('//*[@id="MainContent_tblResident"]/tbody/tr[3]/td[2]').text
        agent_address = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentStreet"]').text
        agent_city = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentCity"]').text
        agent_zip = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentZip"]').text
        agent_country = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentCountry"]').text
        agent_state = browser.find_element_by_xpath('//*[@id="MainContent_lblResidentState"]').text
        # call the csv function and pass the variable
        datatocsv(comp_name,entity_type,file_num,register_date,withdrawal_date,filed_under_state,filed_on_date,principal_address,add_city,add_zip,add_country,add_state,agent_name,agent_address,agent_city,agent_zip,agent_country,agent_state)

    except NoSuchElementException:
        print("some element not found")


def datatocsv(comp_name,entity_type,file_num,register_date,withdrawal_date,filed_under_state,filed_on_date,principal_address,add_city,add_zip,add_country,add_state,agent_name,agent_address,agent_city,agent_zip,agent_country,agent_state):
    with open('mass_by_name.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerow([item] + [comp_name] + [file_num] + [entity_type] + [filed_under_state] + [filed_on_date] + [
            register_date] + [withdrawal_date] + [principal_address] + [add_city] + [add_zip] + [add_country] + [
                            add_state] + [agent_name] + [agent_address] + [agent_city] + [agent_zip] + [agent_state] + [
                            agent_country])
    csvfile.close()
    print ("Complete: ", item)


for item in myNameArray:
    try:
        print ('\n')
        business_url = "http://corp.sec.state.ma.us/CorpWeb/CorpSearch/CorpSearch.aspx"
        browser.get(business_url)
        timeout = 5
        inputElement = browser.find_element_by_xpath('//*[@id="MainContent_txtEntityName"]')

        inputElement.send_keys(item)
        inputElement.send_keys(Keys.RETURN)
        pdb.set_trace()
        # go_button = browser.find_element_by_xpath('//*[@id="MainContent_btnSearch"]')
        # titles_element = browser.find_element_by_xpath('//*[@id="MainContent_SearchControl_grdSearchResultsEntity"]/tbody/tr[2]/td[1]/a').click()
        item = item.replace("\n", "")
        variables()

    except NoSuchElementException:
        print("No agent found with this number!!")
        continue
