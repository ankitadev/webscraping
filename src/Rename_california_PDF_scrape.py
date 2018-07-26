import urllib
import urllib2
from selenium import webdriver
import csv
from selenium.common.exceptions import NoSuchElementException
import collections

option = webdriver.ChromeOptions()
option.add_argument("--incognito")
option.add_argument("--disable-infobars")

browser = webdriver.Chrome(executable_path='../include/chromedriver', chrome_options=option)

myFileNumberArray = open("Untitled5.txt").readlines()


def download_file(download_url, itemnew, newpdf_title_type, newpdf_title_type2, num):
    response = urllib2.urlopen(download_url)
    itemnew = str(itemnew).replace('\n', '')
    one = str(newpdf_title_type2).replace('/', '.')
    string_name = "CA" + "_" + str(itemnew) + "_" + str(one) + "_" + str(newpdf_title_type) + "_" + str(num)
    file = open("%s.pdf" % string_name, "w")
    file.write(response.read())
    file.close()
    print("Completed ", string_name)


for item in myFileNumberArray:
    try:
        print ('\n')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria=" + str(item)
        browser.get(business_url)

        # define all the id's in the browser
        titles_element = browser.find_element_by_xpath("//button[@name='EntityId']")
        titles_element.click()

        registration_key = browser.find_elements_by_xpath("//button[@class='btn btn-link docImage']")
        count = len(registration_key)
        row_count = len(browser.find_elements_by_xpath('//*[@id="docTable"]/tbody/tr'))
        x = 0

        for i in range(0, row_count):
            j = i + 1

            pdf_not_found = browser.find_element_by_xpath('//*[@id="docTable"]/tbody/tr[' + str(j) + ']/td[3]').text
            print ("pdf_not_found", pdf_not_found)

            check_word = str(pdf_not_found).startswith('Image')

            if not check_word:
                print ("DOWNLOAD", i, j, count, row_count, x)
                pdf_title_type = browser.find_element_by_xpath('//*[@id="docTable"]/tbody/tr[' + str(j) + ']/td[1]').text
                pdf_title_type2 = browser.find_element_by_xpath('//*[@id="docTable"]/tbody/tr[' + str(j) + ']/td[2]').text
                pdf_value = registration_key[x].get_attribute("value")
                pdf_url = "https://businesssearch.sos.ca.gov/Document/RetrievePDF?Id=" + str(pdf_value)
                x += 1
                download_file(pdf_url, item, pdf_title_type, pdf_title_type2, i)
            else:
                print "NO PDF"

            # urllib.urlretrieve(pdf_url, "CA"+"_"+item+"_"+str(x)+"_"+"_"+".pdf")

    except NoSuchElementException:
        print("No PDF found in this page!!")
        continue
