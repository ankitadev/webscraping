from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import pdb

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myNameArray = open("Untitled 10.txt").readlines()

for item in myNameArray:
    try:
        print ('\n')
        business_url = "https://icis.corp.delaware.gov/Ecorp/EntitySearch/NameSearch.aspx"
        browser.get(business_url)

        inputElement = browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_frmEntityName"]')
        inputElement.send_keys(item)
        browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_btnSubmit"]').click()
        pdb.set_trace()

    except NoSuchElementException:
        print("No agent found with this number!!")
        continue
