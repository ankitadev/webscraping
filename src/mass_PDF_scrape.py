from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv
import urllib
from selenium.webdriver.common.keys import Keys

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myNameArray = open("Untitled 12.txt").readlines()

for item in myNameArray:
    # get all the COI documents
    view_filings = browser.find_element_by_xpath('//*[@id="MainContent_btnViewFilings"]')
    view_filings.click()

    pdf_url = browser.find_element_by_xpath('//*[@id="MainContent_grdSearchResults"]/tbody/tr[2]/td[6]/a').get_attribute(
        'href')

    urllib.urlretrieve(pdf_url, "MA" + "_" + item + "_" + str(x) + "_" + "_" + ".pdf")