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


def download_file(download_url, itemnew, num):
    response = urllib2.urlopen(download_url)
    itemnew = str(itemnew).replace('\n', '')
    string_name = "California_" + str(itemnew) + "_" + str(num)
    file = open("%s.pdf" % string_name, "w")
    file.write(response.read())
    file.close()
    print("Completed ", string_name)


def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data


for item in myFileNumberArray:
    try:
        print ('\n')
        business_url = "https://businesssearch.sos.ca.gov/CBS/SearchResults?SearchType=NUMBER&SearchCriteria="+str(item)
        browser.get(business_url)

        # define all the id's in the browser
        titles_element = browser.find_element_by_xpath("//button[@name='EntityId']")
        titles_element.click()

        registration_key = browser.find_elements_by_xpath("//button[@class='btn btn-link docImage']")

        for i in range(0, len(registration_key)):
            j = i+1
            pdf_value = registration_key[i].get_attribute("value")
            pdf_title_type = browser.find_element_by_xpath('//*[@id="docTable"]/tbody/tr['+str(j)+']').text
            pdf_url = "https://businesssearch.sos.ca.gov/Document/RetrievePDF?Id=" + str(pdf_value)
            download_file(pdf_url, item, j)
            #urllib.urlretrieve(pdf_url, "California_"+item+"_"+pdf_title_type+".pdf")

            entire_table = browser.find_element_by_xpath('//*[@id="docTable"]').text
            value = convert(entire_table)
            item = str(item).replace('\n', '')

            with open('california_PDF_Stanford_List.csv', 'a') as csvfile:
                writer = csv.writer(csvfile, delimiter=' ')
                writer.writerow(item)
                writer.writerow([value])
            csvfile.close()

    except NoSuchElementException:
        print("No PDF found in this page!!")
        continue

